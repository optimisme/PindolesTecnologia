#!/usr/bin/env python3
"""Compila només guions i SSML revisable. No sintetitza, renderitza ni copia mitjans."""
import hashlib
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

from contingut import LESSONS

ROOT = Path(__file__).resolve().parents[1]
TECHNICAL = ['origin/main','upstream/main','git cherry-pick','git stash push','git stash list',
 'git stash pop','git stash apply','git worktree','git bisect','git remote','git switch',
 'git commit','git merge','git rebase','git restore','git reset','git revert','git add',
 'git status','git diff','git log','git show','git fetch','git push','git pull','git clone',
 'git blame','git reflog','git branch','git tag','pull request','pre-commit','cherry-pick',
 'helloGit.py','notes.md','README.md','app.log','debug.log','GitHub','gitignore','worktree',
 'commits','commit','merge','rebase','restore','revert','reset','reflog','stash','staged',
 'fetch','push','pull','clone','blame','bisect','amend','squash','short','mixed','soft',
 'origin','upstream','main','HEAD','Release','Python','compile','hooks','hook','pick',
 'start','good','bad','yes','pop','apply','add','tag','Git']
TERMS = re.compile(r'(?<![\w])(?:'+ '|'.join(re.escape(x) for x in sorted(TECHNICAL,key=len,reverse=True))+r')(?![\w])',re.I)
SYNTH='http://www.w3.org/2001/10/synthesis'
XML='http://www.w3.org/XML/1998/namespace'


def spoken(text):
    for name,accented in [('salutacio','salutació'),('correccio','correcció'),('recuperacio','recuperació')]:
        text=re.sub(r'\b'+name+r'\b',accented,text)
    pieces=[]
    for index,chunk in enumerate(re.split(r'\[\[(.*?)\]\]',text)):
        if not chunk:continue
        if index%2:pieces.append(dict(lang='en-US',text=chunk));continue
        end=0
        for match in TERMS.finditer(chunk):
            if match.start()>end:pieces.append(dict(lang='ca-ES',text=chunk[end:match.start()]))
            pieces.append(dict(lang='en-US',text=match.group()));end=match.end()
        if end<len(chunk):pieces.append(dict(lang='ca-ES',text=chunk[end:]))
    # Els espais entre dos termes anglesos no han d’esdevenir canvis d’idioma.
    for i in range(1,len(pieces)-1):
        if pieces[i]['text'].isspace() and pieces[i-1]['lang']==pieces[i+1]['lang']=='en-US':
            pieces[i]['lang']='en-US'
    merged=[]
    for part in pieces:
        if merged and merged[-1]['lang']==part['lang']:merged[-1]['text']+=part['text']
        else:merged.append(dict(part))
    return ''.join(p['text'] for p in merged),merged


def clean(text):return re.sub(r'\[\[(.*?)\]\]',r'\1',text)


def ssml(scene,config):
    ET.register_namespace('',SYNTH)
    root=ET.Element(f'{{{SYNTH}}}speak',{'version':'1.0',f'{{{XML}}}lang':'en-US'})
    voice=ET.SubElement(root,f'{{{SYNTH}}}voice',{'name':config['voice']});previous=None
    for beat in scene['beats']:
        ET.SubElement(voice,f'{{{SYNTH}}}bookmark',{'mark':beat['id']})
        for segment in beat['segments']:
            lang=segment['lang']
            if previous and lang!=previous:ET.SubElement(voice,f'{{{SYNTH}}}break',{'time':'500ms'})
            node=ET.SubElement(voice,f'{{{SYNTH}}}lang',{f'{{{XML}}}lang':lang})
            ET.SubElement(node,f'{{{SYNTH}}}prosody',{'rate':config['language_rates'][lang]}).text=segment['text']
            previous=lang
        ET.SubElement(voice,f'{{{SYNTH}}}break',{'time':f"{round(beat['pause_after']*1000)}ms"})
    return ET.tostring(root,encoding='unicode')+'\n'


def make_beat(index,text,visual,pause=3,**extra):
    narration,segments=spoken(text)
    assert '?' not in narration, narration
    assert all(x['text'] for x in segments)
    return dict(id=f'pas_{index:03}',narration=narration,segments=segments,visual=visual,
                pause_after=pause,commands=[],**extra)


def compile_lesson(number,data):
    folder=next(ROOT.glob(f'{number:02}-*'))
    old=json.loads((folder/'episodi.json').read_text())
    config=dict(script_format='git-didactic-v1',status='script_revised_media_unchanged',
                episode_number=number,title=old['title'],series='Píndoles de Git',
                voice='en-US-AndrewMultilingualNeural',language_rates={'ca-ES':'+5%','en-US':'+0%'},
                language_switch_pause_ms=500,questions=False,
                subtitles={'english':'quotes-and-italic','shared_baseline':True},
                music_seconds=4,objective=data['goal'],prerequisites=data['start'],
                timing='Sense marques absolutes: es calcularan amb la futura locució.',scenes=[])
    intro=make_beat(0,old['intro']['narration'],'Número i títol després de la música; mantenir-los fins que acabi la presentació.',2.5)
    config['intro']=dict(narration=intro['narration'],segments=intro['segments'])
    def scene(title,beats,mode='main',input_kind=None):
        item=dict(id=f'rev_{number:02}_{len(config["scenes"]):02}',title=title,mode=mode,beats=beats)
        if input_kind:item['input_kind']=input_kind
        item['narration']=' '.join(b['narration'] for b in beats)
        config['scenes'].append(item)
    counter=0
    def B(text,visual,pause=3,**extra):
        nonlocal counter
        counter+=1;return make_beat(counter,text,visual,pause,**extra)
    scene('Objectiu i punt de partida',[
        B('En aquesta lliçó aprendrem a '+data['goal'][0].lower()+data['goal'][1:], 'Objectiu en una frase; esquema general del resultat.',2.5),
        B(data['start'],'Punt de partida complet amb branca activa, fitxers i estat del treball; fer visible qualsevol cas independent.',3.5)])
    for stage in data['stages']:
        mode=stage['mode'];visual=stage['visual']
        if stage['kind']=='explanation':
            texts=stage['speech'] if isinstance(stage['speech'],list) else [stage['speech']]
            scene(stage['title'],[B(text,visual,stage['pause']) for text in texts],mode)
            continue
        command=stage['command'];beats=[]
        persistent='Mantenir visible el text complet: '+command+'. Conservar l’estat de partida mentre s’explica; encara no executar ni mostrar-ne el resultat.'
        action = ('status' if command.startswith('git -C ') else
                  ' '.join(command.split()[:3]) if command.startswith(('git stash ', 'git bisect ', 'git worktree ', 'git remote add ')) else
                  ' '.join(command.split()[:2]) if command.startswith('git ') else command.split()[0])
        beats.append(B(stage['speech'],persistent+' Subratllar l’acció: '+action+'.',2.5,command_display=command,highlight=action))
        for fragment,explanation in stage['parts']:
            assert fragment in command,(number,command,fragment)
            beats.append(B(explanation,persistent+' Subratllar únicament: '+fragment+'.',2.5,
                           command_display=command,highlight=fragment))
        kind=stage['input_kind']
        execute=B('Introduïm la resposta.' if kind=='interactive' else 'Executem l’ordre.',
                  persistent+' Executar després de la locució, sense mostrar abans el resultat.',1.5,
                  command_display=command,event='execute',effect_after='speech')
        execute['commands']=[command];beats.append(execute)
        beats.append(B(stage['result'],visual+' Mostrar el resultat concret i conservar l’estat anterior per comparar.',3.5,
                       command_display=command,event='result'))
        scene(command,beats,mode,kind)
    scene('Resum final',[B(text,'Tres idees finals; ressaltar només la idea que s’està explicant.',2.5) for text in data['summary']])
    scene('Pràctica final',[B(data['practice'],'Instrucció pràctica completa en pantalla. Mantenir la referència visual final, sense formular preguntes.',4)])
    return folder,config


def markdown(config):
    lines=[f"# Lliçó {config['episode_number']} · {config['title']}",'',
           '**Guió revisat per a la nova producció.** Àudio i vídeo actuals conservats.','',
           '**Locució futura:** Andrew; català +5%, anglès +0%; 500 ms en cada canvi d’idioma, en tots dos sentits.',
           '**Ritme:** pauses de lectura explícites, sense preguntes ni remissions a materials externs.',
           '**Subtítols:** ortografia original; anglès entre cometes i cursiva, amb línia de base comuna.',
           '**Temps:** ordre i pauses definits; les marques absolutes es calcularan després de sintetitzar la veu.','',
           '## Capçalera i presentació','', '4 s de música comuna. Després, llegir el número i el títol:','',
           '> '+config['intro']['narration'],'']
    for scene in config['scenes']:
        lines.extend(['## '+scene['title'],''])
        if scene['mode']!='main':lines.extend(['**Camí:** `'+scene['mode']+'`. Respectar el punt de partida indicat; no encadenar alternatives.',''])
        for beat in scene['beats']:
            if beat.get('command_display'):
                kind=scene.get('input_kind','terminal')
                lines.extend(['**'+('Resposta interactiva' if kind=='interactive' else 'Terminal')+' · comanda completa visible:**','',
                              '```text',beat['command_display'],'```',''])
            if beat.get('highlight'):lines.extend(['**Subratllat:** `'+beat['highlight']+'`.',''])
            lines.extend(['**Locució:** '+beat['narration'],'','**Visual:** '+beat['visual'],'',
                          f"**Pausa:** {beat['pause_after']:g} s sense locució; mantenir el visual i el subratllat.",''])
    return '\n'.join(lines)


def main():
    assert set(LESSONS)==set(range(2,26))
    records=[]
    for number,data in sorted(LESSONS.items()):
        folder,config=compile_lesson(number,data)
        for scene in config['scenes']:
            assert scene['narration']==' '.join(b['narration'] for b in scene['beats'])
            for b in scene['beats']:
                assert b['narration']==''.join(s['text'] for s in b['segments'])
            ET.fromstring(ssml(scene,config))
        (folder/'guio-revisat.json').write_text(json.dumps(config,ensure_ascii=False,indent=2)+'\n')
        (folder/'guio-revisat.md').write_text(markdown(config))
        beats=[b for s in config['scenes'] for b in s['beats']]
        record=dict(episode=folder.name,title=config['title'],scenes=len(config['scenes']),beats=len(beats),
                    words=sum(len(b['narration'].split()) for b in beats),
                    reading_pause_seconds=sum(b['pause_after'] for b in beats),
                    script_sha256=hashlib.sha256((folder/'guio-revisat.json').read_bytes()).hexdigest())
        records.append(record)
    lines=['# Guions revisats · lliçons 2–25','',
           'Els 24 guions estan reescrits amb explicacions per passos, comandes desglossades, pauses i cap pregunta.',
           'Aquesta revisió només modifica documents. Les locucions i els vídeos existents es conserven.',
           'Cada carpeta té `guio-revisat.md` per llegir i `guio-revisat.json` amb els passos i idiomes explícits.',
           'Els `episodi.json` i `guio.md` publicats es mantenen vinculats als mitjans actuals.',
           'La futura producció haurà d’adaptar els visuals a aquests passos i obtenir els temps reals del nou àudio.','',
           '| Lliçó | Guió revisat | Escenes | Passos | Paraules |','| --- | --- | ---: | ---: | ---: |']
    for r in records:lines.append(f"| {r['episode']} | [Llegir](../{r['episode']}/guio-revisat.md) | {r['scenes']} | {r['beats']} | {r['words']} |")
    lines.extend(['','## Edició i comprovació','',
                  '`contingut.py` conté el text editorial i les instruccions de cada lliçó.',
                  'Des de la carpeta `vids`, `python3 guions/compila.py` actualitza només els guions revisats.',
                  'No carrega credencials, no contacta cap sintetitzador i no modifica les carpetes audio o output.',
                  'Per validar els idiomes, les opcions, els subtítols i els 748 arxius conservats: `.venv/bin/python guions/verifica.py`.',''])
    (ROOT/'guions/README.md').write_text('\n'.join(lines))
    (ROOT/'guions/revisio.json').write_text(json.dumps(dict(status='scripts_revised_no_media_generated',episodes=records),ensure_ascii=False,indent=2)+'\n')
    print('Compilats',len(records),'guions;',sum(r['beats'] for r in records),'passos. Cap àudio generat.')


if __name__=='__main__':main()
