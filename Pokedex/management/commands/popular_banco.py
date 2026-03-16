import requests
from django.core.management.base import BaseCommand
from ...models import Pokemon, Tipo

class Command(BaseCommand):
    def handle(self,*args,**kwargs):
        self.stdout.write('Iniciando População do Banco de Dados')

        url = 'https://pokeapi.co/api/v2/pokemon?limit=151&offset=0'
        lista = requests.get(url).json()['results']

        for i, item in enumerate(lista, start=1):
            nome = item['name']

            if Pokemon.objects.filter(numero=i).exists():
                self.stdout.write(f'    #{i:03d}    {nome} - já existe, pulando')
                continue

            self.stdout.write(f'  Buscando #{i:03d} {nome}...')

            dados = requests.get(item['url']).json()
            species = requests.get(dados['species']['url']).json()

            descricao = ''
            for entry in species['flavor_text_entries']:
                if entry['language']['name'] == 'en':
                    descricao = entry['flavor_text'].replace('\n', ' ').replace('\f', ' ')
                    break

            stats = {}

            for stat in dados['stats']:
                stats[stat['stat']['name']] = stat['base_stat']
                

            pokemon = Pokemon.objects.create(

                numero = dados['id'],
                nome = dados['name'].capitalize(),
                descricao = descricao,
                foto_url = dados['sprites']['other']['official-artwork']['front_default'],
                foto_shiny = dados['sprites']['other']['official-artwork']['front_default'] or '',
                altura = dados['height'] /10,
                peso = dados['weight'] /10,
                hp = stats['hp'],
                ataque = stats['attack'],
                defesa = stats['defense'],
                ataque_especial = stats['special-attack'],
                defesa_especial = stats['special-defense'],
                velocidade = stats['speed'],

                )

            
            for tipos in dados['types']:
                tipo , criado = Tipo.objects.get_or_create(nome=tipos['type']['name'])
                pokemon.tipos.add(tipo)

        self.stdout.write(self.style.SUCCESS('Banco populado com sucesso! ✅'))
            