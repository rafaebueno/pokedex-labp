pokedex = []
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
      'nivel': nivel_Pokemon}
    pokedex.append(pokemon)
    escolha_input = input('Deseja adicionar outro Pokemon?\nSIM/NÃO: ').upper()
    escolha = escolha_input
  return pokedex


def listar_pokemon():
    for c in range(0, len(pokedex)):
         print(pokedex[c])
    print(f'A quantidade de Pokemóns cadastrados é de: {len(pokedex)}')