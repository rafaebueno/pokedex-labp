import pokefunc


def menu():
  while (1):
    print("-- Menu Inicial --")
    print(" 1 - Adicionar um novo Pokémon")
    print(" 2 - Listar todos os Pokémon")
    print(" 3 - Atualizar informações de um Pokémon existente na Pokedex")
    print(" 4 - Excluir Pokémon da Pokedex")
    print(" 5 - Consulta por Nome")
    print(" 6 - Consulta por Tipo")
    print(" 7 - Contar Pokemóns na Pokedéx")
    print(" 8 - Salvar e Sair")

    opcao = int(input("Digite a sua opção: "))

    if opcao == 1:
        pokefunc.AddPoke()

    elif opcao == 2:
        pokefunc.listar_pokemon()

    elif opcao == 3:
        id = int(input('Digite o ID do Pokemón à ser atualizado: '))
        nome = str(input('Qual o nome à ser substituído? ')).upper()
        tipo = str(input('Qual o tipo do Pokemón? ')).upper()
        nivel = float(input('Qual o Nível do Pokemón? '))
        pokefunc.atualizarPokemon(id, nome, tipo, nivel)


    elif opcao == 4:
        print('Qual Pokemón você deseja excluir?')
        pokefunc.listar_pokemon()
        id = int(input('Digite o ID do Pokemón à ser excluído: '))
        pokefunc.excluir_pokemon(id)

    elif opcao == 5: #consulta nome
        nome = str(input('Digite o Nome do Pokemón a ser pesquisado: ')).upper()
        pokefunc.pesquisaPokemonNome(nome)

    elif opcao == 6: #consulta tipo
        tipo = str(input('Digite o Tipo do Pokemón a ser pesquisado: ')).upper()
        pokefunc.pesquisaPokemonTipo(tipo)
    
    elif opcao == 7: 
        pokefunc.contarPokemon()

    elif opcao == 8:
        pokefunc.salvar_pokedex('pokedex')   

    else:
        print("FALTA PROGRAMAR ESSA PARTE")
