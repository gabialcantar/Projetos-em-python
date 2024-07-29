# Sistema de gerenciamento de despesas

# Lista para armazenar as despesas
despesas = []

# Função para adicionar uma despesa
def adicionar_despesa(nome, valor):
    despesa = {"nome": nome, "valor": valor}
    despesas.append(despesa)
    print(f"Despesa '{nome}' no valor de {valor} adicionada com sucesso!")

# Função para listar todas as despesas
def listar_despesas():
    if not despesas:
        print("Nenhuma despesa cadastrada.")
    else:
        for despesa in despesas:
            print(f"Nome: {despesa['nome']}, Valor: {despesa['valor']}")

# Função para calcular o total de despesas
def total_despesas():
    total = sum(despesa['valor'] for despesa in despesas)
    print(f"Total de despesas: {total}")

# Menu de opções
def menu():
    while True:
        print("\nSistema de Gerenciamento de Despesas")
        print("1. Adicionar Despesa")
        print("2. Listar Despesas")
        print("3. Total de Despesas")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Digite o nome da despesa: ")
            valor = float(input("Digite o valor da despesa: "))
            adicionar_despesa(nome, valor)
        elif opcao == "2":
            listar_despesas()
        elif opcao == "3":
            total_despesas()
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
menu()