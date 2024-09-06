class ContaBancaria:
    def _init_(self, numero_conta, titular, saldo_inicial=0):
        self.numero_conta=numero_conta
        self.titular=titular
        self.saldo=saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor: .2f} realizado com sucesso!")
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self,valor):
        if valor>0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso!")
            else:
                print("Saldo insuficiente.")
        else:
                 print("Valor do saque deve ser positivo")
        def ver_saldo(self):
         print(f"saldo atual: R${self.saldo: .f}")
