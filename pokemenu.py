import pokefunc

def menu():
  while (1):
      print("-- Menu Inicial --")
      print(" 1 - Adicionar um novo Pokémon")
      print(" 2 - Listar todos os Pokémon")
      print(" 3 - Atualizar informações de um Pokémon existente na Pokedex")
      print(" 4 - Excluir Pokémon da Pokedex")
      print(" 5 - Consultar Pokémon na Pokedéx")
      print(" 6 - Salvar e Sair")

      opcao = int(input("Digite a sua opção:"))

      if opcao == 1:
         pokefunc.AddPoke()

      elif opcao == 2:
          pokefunc.listar_pokemon()

      elif opcao == 3:
          print("FALTA PROGRAMAR ESSA PARTE")

      elif opcao == 4:
          PokemonExcluir = int(input('Digite o ID do Pokemón que deseja excluir: '))
          pokefunc.excluir_pokemon(PokemonExcluir)

      elif opcao == 5: 
          idPesquisa = int(input('Digite o ID do Pokemón a ser pesquisado: '))
          pokefunc.pesquisaPokemon(idPesquisa)

      elif opcao == 6:
          print("FALTA PROGRAMAR ESSA PARTE")
          
      else:
          print("Opção inválida \n")