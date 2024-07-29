class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo=0, limite_cheque_especial=500):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo
        self.limite_cheque_especial = limite_cheque_especial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0:
            if self.saldo + self.limite_cheque_especial >= valor:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente, mesmo com o limite de cheque especial.")
        else:
            print("Valor de saque deve ser positivo.")

    def verificar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")
        print(f"Limite de cheque especial disponível: R${self.limite_cheque_especial + self.saldo:.2f}")

def main():
    # Criar uma conta bancária de exemplo
    conta = ContaBancaria(numero_conta="12345", titular="João Silva", saldo=100)
    
    while True:
        print("\nSistema Bancário Simples")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Verificar saldo")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            valor = float(input("Valor a depositar: "))
            conta.depositar(valor)
        
        elif opcao == '2':
            valor = float(input("Valor a sacar: "))
            conta.sacar(valor)
        
        elif opcao == '3':
            conta.verificar_saldo()
        
        elif opcao == '4':
            print("Saindo do sistema bancário...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
