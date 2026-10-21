"""Prepara un SSML d’Andrew amb tots els fragments etiquetats explícitament."""
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parent
SYNTH='http://www.w3.org/2001/10/synthesis'
XML='http://www.w3.org/XML/1998/namespace'


def variant_suffix(pause_ms=0,language_rates=None):
    if not isinstance(pause_ms,int) or pause_ms<0:
        raise ValueError('La pausa ha de ser un nombre enter de mil·lisegons igual o superior a zero.')
    suffix=f'-pauses-{pause_ms}ms' if pause_ms else ''
    if language_rates:
        if set(language_rates)!={'ca-ES','en-US'}:
            raise ValueError('Cal indicar una velocitat per a ca-ES i una per a en-US.')
        values=[]
        for lang,label in (('ca-ES','ca'),('en-US','en')):
            rate=language_rates[lang]
            if not re.fullmatch(r'[+-]?\d+%',rate):
                raise ValueError('Les velocitats han de ser percentatges enters, com +8% o +0%.')
            value=int(rate[:-1])
            if not -50<=value<=100:raise ValueError('La velocitat ha d’estar entre -50% i +100%.')
            values.append(f'{label}{"menys" if value<0 else ""}{abs(value)}')
        suffix+='-'+ '-'.join(values)
    return suffix


def prepare(pause_ms=0):
    config=json.loads((ROOT/'mostra.json').read_text())
    language_rates=config.get('language_rates')
    suffix=variant_suffix(pause_ms,language_rates)
    assert config['voice']=='en-US-AndrewMultilingualNeural'
    assert {segment['lang'] for segment in config['segments']}=={'ca-ES','en-US'}
    ET.register_namespace('',SYNTH)
    speak=ET.Element(f'{{{SYNTH}}}speak',{'version':'1.0',f'{{{XML}}}lang':'en-US'})
    voice=ET.SubElement(speak,f'{{{SYNTH}}}voice',{'name':config['voice']})
    container=voice if language_rates else ET.SubElement(voice,f'{{{SYNTH}}}prosody',{'rate':config['rate']})
    for index,segment in enumerate(config['segments']):
        if pause_ms and index and config['segments'][index-1]['lang']!=segment['lang']:
            ET.SubElement(container,f'{{{SYNTH}}}break',{'time':f'{pause_ms}ms'})
        node=ET.SubElement(container,f'{{{SYNTH}}}lang',{f'{{{XML}}}lang':segment['lang']})
        if language_rates:
            node=ET.SubElement(node,f'{{{SYNTH}}}prosody',{'rate':language_rates[segment['lang']]})
        node.text=segment['text']
    ET.indent(speak,space='  ')
    # El format XML no ha d’afegir espais dins dels fragments parlats.
    if language_rates:
        for node in speak.findall(f'.//{{{SYNTH}}}lang'):
            node.text=None
            node[0].tail=None
    ssml=ET.tostring(speak,encoding='unicode')+'\n'
    (ROOT/f'prova{suffix}.ssml').write_text(ssml)
    parsed=ET.fromstring(ssml)
    assert len(parsed.findall(f'.//{{{SYNTH}}}voice'))==1
    languages=parsed.findall(f'.//{{{SYNTH}}}lang')
    assert len(languages)==len(config['segments'])
    for node,segment in zip(languages,config['segments']):
        assert node.attrib[f'{{{XML}}}lang']==segment['lang'] and ''.join(node.itertext())==segment['text']
        if language_rates:
            assert node[0].attrib['rate']==language_rates[segment['lang']]
    switches=sum(a['lang']!=b['lang'] for a,b in zip(config['segments'],config['segments'][1:]))
    breaks=parsed.findall(f'.//{{{SYNTH}}}break')
    assert len(breaks)==(switches if pause_ms else 0)
    assert all(node.attrib=={'time':f'{pause_ms}ms'} for node in breaks)
    lines=['# Guió de la prova amb idiomes explícits','',
           'Una sola veu: AndrewMultilingual. Català i anglès marcats amb SSML.','']
    if language_rates:
        lines += [f'Velocitats: català {language_rates["ca-ES"]}; anglès {language_rates["en-US"]}.','']
    if pause_ms:
        lines += [f'Pausa explícita de {pause_ms} ms a cadascun dels {switches} canvis d’idioma.',
                  'Sense pauses afegides al principi ni al final.','']
    for segment in config['segments']:
        label='Català' if segment['lang']=='ca-ES' else 'Anglès'
        lines.append(f'- **{label}:** {segment["text"].strip()}')
    (ROOT/f'guio{suffix}.md').write_text('\n'.join(lines)+'\n')
    return config,ssml


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pausa-ms',type=int,default=0)
    args=parser.parse_args()
    if args.pausa_ms<0:parser.error('--pausa-ms ha de ser igual o superior a zero')
    config,_=prepare(args.pausa_ms)
    print('SSML vàlid: una sola veu Andrew, 7 fragments catalans i 6 anglesos explícits.')
    print(ROOT/f'prova{variant_suffix(args.pausa_ms,config.get("language_rates"))}.ssml')
