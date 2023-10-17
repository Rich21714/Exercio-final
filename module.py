contatos = []

def adicionar_contato():
    nome = input("Nome do contato: ")
    telefone = input("Telefone: ")
    email = input("Email: ")

    if "@" in email:
        contato = {"nome": nome, "telefone": telefone, "email": email}
        contatos.append(contato)
        print("Contato adicionado com sucesso!")
    else:
        print("O email não é válido. Certifique-se de incluir o '@' no endereço de email.")

def listar_contatos():
    if contatos:
        for contato in contatos:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")
    else:
        print("Lista de contatos vazia.")

def buscar_contato():
    nome = input("Digite o nome do contato que deseja buscar: ")
    for contato in contatos:
        if contato["nome"] == nome:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")
            return
    print(f"Contato com o nome '{nome}' não encontrado.")

def remover_contato():
    nome = input("Digite o nome do contato que deseja remover: ")
    for contato in contatos:
        if contato["nome"] == nome:
            contatos.remove(contato)
            print(f"Contato '{nome}' removido com sucesso.")
            return
    print(f"Contato com o nome '{nome}' não encontrado.")

