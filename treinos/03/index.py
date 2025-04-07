def exibir_menu():
    print("\nAgenda de Contatos")
    print("1. Adicionar Contato")
    print("2. Exibir Contatos")
    print("3. Editar Contato")
    print("4. Excluir Contato")
    print("5. Sair")

def adicionar_contato(agenda):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o e-mail do contato: ")
    
    agenda[nome] = {"telefone": telefone, "email": email}
    print(f"Contato {nome} adicionado com sucesso!")

def exibir_contatos(agenda):
    if not agenda:
        print("Não há contatos na agenda.")
    else:
        print("\nContatos:")
        for nome, info in agenda.items():
            print(f"Nome: {nome}")
            print(f"Telefone: {info['telefone']}")
            print(f"E-mail: {info['email']}")
            print("-" * 30)

def editar_contato(agenda):
    nome = input("Digite o nome do contato a ser editado: ")
    if nome in agenda:
        telefone = input(f"Novo telefone para {nome} (atual: {agenda[nome]['telefone']}): ")
        email = input(f"Novo e-mail para {nome} (atual: {agenda[nome]['email']}): ")
        
        agenda[nome] = {"telefone": telefone, "email": email}
        print(f"Contato {nome} atualizado com sucesso!")
    else:
        print("Contato não encontrado!")

def excluir_contato(agenda):
    nome = input("Digite o nome do contato a ser excluído: ")
    if nome in agenda:
        del agenda[nome]
        print(f"Contato {nome} excluído com sucesso!")
    else:
        print("Contato não encontrado!")

def main():
    agenda = {}
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_contato(agenda)
        elif opcao == "2":
            exibir_contatos(agenda)
        elif opcao == "3":
            editar_contato(agenda)
        elif opcao == "4":
            excluir_contato(agenda)
        elif opcao == "5":
            print("Saindo da agenda...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
