"""Comparació curta de GitHub amb Enric i una referència anglesa."""
import asyncio
import json
from pathlib import Path
import genera_mostra as sample

async def main():
    sample.ROOT = Path(__file__).resolve().parent/'github'
    (sample.ROOT/'output').mkdir(parents=True,exist_ok=True)
    config = {'voice':'ca-ES-EnricNeural','rate':'+12%'}
    forms = [('01-original','GitHub allotja repositoris a internet.'),
             ('02-jab','Guit jab allotja repositoris a internet.'),
             ('03-hab','Guit hàb allotja repositoris a internet.')]
    await asyncio.gather(*[sample.voice(name,text,config) for name,text in forms])
    await sample.voice('04-angles','GitHub.',{'voice':'en-US-GuyNeural','rate':'+0%'})
    (sample.ROOT/'mostres.json').write_text(json.dumps({'catalan':config,'variants':forms,'english_reference':{'voice':'en-US-GuyNeural','text':'GitHub.'}},ensure_ascii=False,indent=2))

if __name__=='__main__':asyncio.run(main())
