import io
import os
#1
pokedex = {}

def AddPoke():
  escolha = 'SIM'
  while escolha == 'SIM':
    identificacao = len(pokedex) + 1
    pokemon_Nome = str(input('Digite o nome do Pokemon: ')).upper()
    tipo_Pokemon = str(input('Digite o tipo do Pokemon: ')).upper()
    nivel_Pokemon = float(input('Digite o nível do Pokemon: '))

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

#2
def listar_pokemon():
  # Itera sobre os Pokémon na Pokedex
  for identificacao, pokemon in pokedex.items():
    # Exibe as informações do Pokémon
    print(f'|ID: {identificacao}|Nome: {pokemon["nome"]}|Tipo: {pokemon["tipo"]} |Nível: {pokemon["nivel"]}|')

#3
def excluir_pokemon(id):
  del pokedex[id]
  print('Pokemón deletado com sucesso')

#4
def atualizarPokemon(id, nome, tipo, nivel):
  pokemon = pokedex[id]
  pokemon['nome'] = nome
  pokemon['tipo'] = tipo
  pokemon['nivel'] = nivel

#5
def pesquisaPokemonNome(nome):
  for identificacao, pokemon in pokedex.items():
    if pokemon['nome'] == nome:
      print(f'| ID: {pokemon["id"]} | Nome: {pokemon["nome"]} | Tipo: {pokemon["tipo"]} | Nivel: {pokemon["nivel"]} |')

#6
def pesquisaPokemonTipo(tipo):
  for identificacao, pokemon in pokedex.items():
    if pokemon['tipo'] == tipo:
      print(f'| ID: {pokemon["id"]} | Nome: {pokemon["nome"]} | Tipo: {pokemon["tipo"]} | Nivel: {pokemon["nivel"]} |')
#7
def contarPokemon():
  print(f'A quantidade de Pokemóns registrados são de {len(pokedex)} Pokemóns')


#8
def importar_pokedex(nome_arquivo):
    arquivo = "pokedex.txt"

    # Abre o arquivo e lê as informações existentes
    with open(arquivo, 'r') as arquivo:
        for linha in arquivo:
            # Converte a linha em um dicionário
            pokemon = dict(zip(["id", "nome", "tipo", "nivel"], linha.split(",")))

            # Adiciona o Pokémon à lista principal
            pokedex.update({pokemon["id"]: pokemon})

    return pokedex

# Função para criar um novo registro no banco de dados (arquivo de texto)
def criar_registro(nome_arquivo):
    arquivo = "pokedex.txt"
    lista_de_pokemons = []
    for identificador, pokemon in pokedex.items():
        lista_de_pokemons.append(f'{pokemon["id"]}, {pokemon["nome"]}, {pokemon["tipo"]}, {pokemon["nivel"]}\n')

    string_de_pokemons = ''.join(lista_de_pokemons)

    try:
        with open(nome_arquivo, 'a') as arquivo:
            arquivo.write(string_de_pokemons)
        print('Registro criado com sucesso.')
    except IOError as e:
        print(f"Erro ao criar o registro: {e}")

# Função para listar todos os registros no banco de dados
def listar_registros(nome_arquivo):
    arquivo = "pokedex.txt"
    try:
        with open(nome_arquivo, 'r') as arquivo:
            registros = arquivo.readlines()
            for i, registro in enumerate(registros):
                print(f'Registro {i + 1}: {registro.strip()}')
    except IOError as e:
        print(f"Erro ao listar os registros: {e}")


# Função para atualizar um registro no banco de dados (arquivo de texto)
def atualizar_registro(nome_arquivo, registro_antigo, novo_registro):
    arquivo = "pokedex.txt"
    try:
        with open(nome_arquivo, 'r') as arquivo:
            registros = arquivo.readlines()

        encontrou = False
        for i, registro in enumerate(registros):
            if registro.strip() == registro_antigo:
                registros[i] = novo_registro + '\n'
                encontrou = True
                break

        if encontrou:
            with open(nome_arquivo, 'w') as arquivo:
                arquivo.writelines(registros)
            print('Registro atualizado com sucesso.')
        else:
            print('Registro não encontrado.')

    except IOError as e:
        print(f"Erro ao atualizar o registro: {e}")

def apagar_salvamento_antigo():
    arquivo = "pokedex.txt"
    try:
        with open(arquivo, 'w'):
            pass
    except IOError as e:
        print(f"Erro ao apagar o salvamento antigo: {e}")
