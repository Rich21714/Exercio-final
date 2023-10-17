from module import *

while True:
    print("\nEscolha uma opção:")
    print("1) Adicionar um novo contato")
    print("2) Listar todos os contatos")
    print("3) Buscar um contato pelo nome")
    print("4) Remover um contato pelo nome")
    print("5) Sair do programa")

    opcao = input("Digite o número da opção desejada: ")

    match opcao:
            
        case "1":
            adicionar_contato()
        case "2":
            listar_contatos()
        case "3":
            buscar_contato()
        case "4":
            remover_contato()
        case "5":
            print("Saindo do programa. Até logo!")
            break
        case _:
            print("Opção inválida. Por favor, escolha uma opção válida.")