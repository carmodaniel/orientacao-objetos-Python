# Orientação a objetos
# criação da classe
class ContaCorrente:

    def __init__(self, nome, cpf): # O método __init__ é chamado quando um objeto é criado. Ele inicializa os atributos da instância.
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None

    # Criação de metodos
    def consultar_saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self.saldo))

    def deposita(self, valor): #metodo depositar
        self.saldo += valor

    def _limite_conta(self): #metodo limite conta interno para ser urtilizado dentro da calsse
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self, valor): #metodo sacar
        if self.saldo - valor < self._limite_conta(): # utilizando o metodo limite_conta para validar limite
            print("Você não tem Saldo suficiente para sacar esse valor")
            self.consultar_saldo() # utilizando o metodo consultar_saldo para validar saldo
        else:
            self.saldo -= valor

    def consulta_limite_chequeespecial(self):
        print('Seu límite de cheque especial é de R${:,.2f}'.format(self._limite_conta())) #metodo consulta cheque especial

# programa
conta = ContaCorrente("Daniel", "111.111.111-00")

## depositando dinheiro
conta.deposita(10000) # utilizando metodo depositar
conta.consultar_saldo() # utilizando metodo consultar


## sacando dinheir
conta.sacar_dinheiro(10500) # utilizando sacar dinheiro

print('Saldo Final')
conta.consultar_saldo() # utilizando metodo consultar
conta.consulta_limite_chequeespecial()  # utilizando limite chequeespecial


