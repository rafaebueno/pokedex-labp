from collections.abc import KeysView

pokedex = {}


def AddPoke():
  escolha = 'SIM'
  while escolha == 'SIM':
    identificacao = len(pokedex) + 1
    pokemon_Nome = str(input('Digite o nome do Pokemon: ')).upper()
    tipo_Pokemon = str(input('Digite o tipo do Pokemon: ')).upper()
    nivel_Pokemon = int(input('Digite o nível do Pokemon: '))

    pokemon = {
        'id': identificacao,
        'nome': pokemon_Nome,
        'tipo': tipo_Pokemon,
        'nivel': nivel_Pokemon
    }

    pokedex[identificacao] = pokemon
    escolha_input = input('Deseja adicionar outro Pokemon?\nSIM/NÃO: ').upper()
    escolha = escolha_input
  return pokedex

def listar_pokemon():
  # Itera sobre os Pokémon na Pokedex
  for identificacao, pokemon in pokedex.items():
    # Exibe as informações do Pokémon
    print(
        f'|ID: {identificacao:3}| Nome: {pokemon["nome"]:10}|Tipo: {pokemon["tipo"]:10} | Nível: {pokemon["nivel"]:3} |'
    )


def excluir_pokemon(id):
  id_excluir = id - 1
  del pokedex[id]


def pesquisaPokemon(id):
  print(pokedex[id - 1])
