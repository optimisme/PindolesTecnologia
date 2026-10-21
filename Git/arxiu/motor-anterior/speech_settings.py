"""Configuració privada de Speech; mai imprimeix ni desa la clau."""
from pathlib import Path
import os
from urllib.parse import urlparse
import re

ROOT = Path(__file__).resolve().parent
ALLOWED = {f'{prefix}_{name}' for prefix in ('AZURE_SPEECH', 'SPEECH')
           for name in ('KEY', 'ENDPOINT', 'REGION')}


def load_speech_environment():
    path = ROOT / '.env'
    if not path.exists():
        return
    from dotenv import dotenv_values
    from dotenv.parser import parse_stream
    # Validació sense incloure el contingut de cap línia en errors o registres.
    with path.open() as stream:
        for binding in parse_stream(stream):
            if binding.error:
                raise ValueError(f'.env invàlid a la línia {binding.original.line}.')
            if binding.key and binding.key not in ALLOWED:
                raise ValueError('.env conté una variable no admesa per a Speech.')
    # Tracta el fitxer com a dades: no executa ordres ni expandeix ${variables}.
    values = dotenv_values(path, interpolate=False)
    for key, value in values.items():
        if value and not os.environ.get(key):
            os.environ[key] = value


def connection_options(target):
    if target.startswith('https://'):
        parsed = urlparse(target)
        if (not parsed.hostname or not parsed.hostname.endswith('.cognitiveservices.azure.com')
                or parsed.username or parsed.password or parsed.query or parsed.fragment
                or parsed.path not in ('', '/') or parsed.port not in (None, 443)):
            raise ValueError('Cal l’endpoint base HTTPS de Speech, sense cap ruta de projecte.')
        return {'endpoint': f'https://{parsed.hostname}/'}
    if re.fullmatch(r'[a-z0-9-]+', target):
        return {'region': target}
    raise ValueError('Endpoint o regió de Speech invàlids.')


def credentials(default_endpoint=None):
    load_speech_environment()
    key = os.environ.get('AZURE_SPEECH_KEY') or os.environ.get('SPEECH_KEY')
    target = (os.environ.get('AZURE_SPEECH_ENDPOINT') or os.environ.get('SPEECH_ENDPOINT')
              or os.environ.get('AZURE_SPEECH_REGION') or os.environ.get('SPEECH_REGION')
              or default_endpoint)
    if not key or not key.strip():
        raise RuntimeError('Falta AZURE_SPEECH_KEY al fitxer local 01-Git/vids/.env.')
    if not target:
        raise RuntimeError('Falta AZURE_SPEECH_ENDPOINT o AZURE_SPEECH_REGION.')
    return key.strip(), connection_options(target)
