import pokefunc

def menu():
  while (1):
      print("-- Menu Inicial --")
      print(" 1 - Adicionar um novo Pokémon")
      print(" 2 - Listar todos os Pokémon")
      print(" 3 - Atualizar informações de um Pokémon existente na Pokedex")
      print(" 4 - Excluir Pokémon da Pokedex")
      print(" 5 - Consultar Pokémon na Pokedéx")
      print(" 7 - Salvar e Sair")

      opcao = int(input("Digite a sua opção:"))

      if opcao == 1:
         pokefunc.AddPoke()

      elif opcao == 2:
          pokefunc.listar_pokemon()

      elif opcao == 3:
          print("Olá")

      elif opcao == 4:
          print("Olá")

      elif opcao == 5:
            pesquisar_poke = str(input('Você quer pesquisar pelo NOME ou TIPO do Pokemón?\n')).upper()

            if pesquisar_poke == 'NOME':
                nome_poke = str(input('Digite o NOME do Pokemon que deseja pesquisar: '))
                pokefunc.pesquisar_pokemon_nome(nome_poke)
            elif pesquisar_poke == 'TIPO':
                tipo_poke = int(input('Digite o NOME do Pokemon que deseja pesquisar: '))
                pokefunc.pesquisar_pokemon_tipo(tipo_poke)
            else:
                print(f'Essa opção não é aceita!')

      elif opcao == 6:
          print("Olá")

      elif opcao == 7:
          print("Olá")

      elif opcao == 8:
          print("Olá")

      else:
          print("Opção inválida \n")