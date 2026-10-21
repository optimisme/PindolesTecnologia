"""Lectura de serie.yaml i dels fitxers llico.yaml en l’ordre de la sèrie."""
import argparse
from pathlib import Path

import yaml

ORDINALS = ['zero', 'Primera', 'Segona', 'Tercera', 'Quarta', 'Cinquena', 'Sisena', 'Setena',
            'Vuitena', 'Novena', 'Desena', 'Onzena', 'Dotzena', 'Tretzena', 'Catorzena',
            'Quinzena', 'Setzena', 'Dissetena', 'Divuitena', 'Dinovena', 'Vintena',
            'Vint-i-unena', 'Vint-i-dosena', 'Vint-i-tresena', 'Vint-i-quatrena',
            'Vint-i-cinquena', 'Vint-i-sisena', 'Vint-i-setena', 'Vint-i-vuitena',
            'Vint-i-novena', 'Trentena', 'Trenta-unena', 'Trenta-dosena', 'Trenta-tresena',
            'Trenta-quatrena', 'Trenta-cinquena']


def spoken_number(number):
    """«Lliçó zero» o «Vuitena lliçó», tal com s’anuncia després de la sintonia."""
    return 'Lliçó zero' if number == 0 else f'{ORDINALS[number]} lliçó'


def load_yaml(path):
    with Path(path).open(encoding='utf-8') as source:
        return yaml.safe_load(source)


def find_folder(root, slug):
    matches = sorted(root.glob(f'[0-9][0-9]-{slug}'))
    if len(matches) != 1:
        raise FileNotFoundError(f'Cal exactament una carpeta NN-{slug} a {root}; n’hi ha {len(matches)}.')
    return matches[0]


def load_series(folder):
    folder = Path(folder).resolve()
    data = load_yaml(folder/'serie.yaml')
    lessons = []
    for number, slug in enumerate(data['llicons']):
        path = find_folder(folder, slug)
        lesson = load_yaml(path/'llico.yaml') if (path/'llico.yaml').exists() else {}
        lessons.append({'number': number, 'folder': path, 'slug': slug, 'name': f'{number:02}-{slug}',
                        'card': lesson.get('capcalera', [slug.upper(), '']), 'data': lesson})
    return {'root': folder, 'name': data['nom'], 'config': data, 'lessons': lessons}


def renumber(folder):
    """Reanomena les carpetes NN-nom segons l’ordre de serie.yaml, en dues passes."""
    series = load_series(folder)
    moves = [(item['folder'], item['folder'].with_name(item['name'])) for item in series['lessons']
             if item['folder'].name != item['name']]
    temporary = []
    for source, target in moves:
        middle = source.with_name(source.name+'.renumera')
        source.rename(middle)
        temporary.append((middle, target))
    for middle, target in temporary:
        assert not target.exists(), target
        middle.rename(target)
        print(f'{middle.name[:-len(".renumera")]} → {target.name}')
    if not moves:
        print('Les carpetes ja segueixen l’ordre de la sèrie.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('serie', type=Path)
    parser.add_argument('--renumera', action='store_true',
                        help='Reanomena les carpetes perquè el número coincideixi amb l’ordre')
    args = parser.parse_args()
    if args.renumera:
        renumber(args.serie)
    else:
        for item in load_series(args.serie)['lessons']:
            print(item['name'], '·', ' — '.join(item['card']))
