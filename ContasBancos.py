# Orientação a objetos
from datetime import datetime # biblioteca para pegar data e hora
import pytz # biblioteca para formatação de suso


# criação da classe
class ContaCorrente:

    @staticmethod  # O @staticmethod em Python é um decorador usado para definir um método estático dentro de uma classe. Vamos entender o que isso significa:
    def _data_hora():  # Um método estático é uma função que pertence à classe, mas não depende de instâncias específicas (objetos) dessa classe
        fuso_br = pytz.timezone('Brazil/East') #  utilzando pytz.timezone para pegar timezone do brasil
        horario_br = datetime.now(fuso_br)
        return horario_br.strftime('%d/%m/%Y %H:%M:%S') # utilzando strftime para formatar data e hora em dia/mes/Ano Hora:Minuto:Segundo

    def __init__(self, nome, cpf, agencia, num_conta):  # O método __init__ é chamado quando um objeto é criado. Ele inicializa os atributos da instância.
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []

    # Criação de metodos
    def consultar_saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self.saldo))

    def deposita(self, valor):  # metodo depositar
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):  # metodo limite conta interno para ser urtilizado dentro da classe
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self, valor):  # metodo sacar
        if self.saldo - valor < self._limite_conta():  # utilizando o metodo limite_conta para validar limite
            print("Você não tem Saldo suficiente para sacar esse valor")
        else:
            self.saldo -= valor
            self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))

    def consulta_limite_chequeespecial(self):  # metodo consulta cheque especial
        print('Seu límite de cheque especial é de R${:,.2f}'.format(
            self._limite_conta()))

    def consultar_historico_transacoes(self):  # metodo para historico de transação
        print('Histórico de Transaç es')
        print('Valor, Saldo, Data e Hora')
        for transacao in  self.transacoes:
            print(transacao)


#  programa
conta = ContaCorrente("Daniel", "111.111.111-00", 123456, 34062)

# depositando dinheiro
conta.deposita(10000)  # utilizando metodo depositar
conta.consultar_saldo()  # utilizando metodo consultar

#  sacando dinheir
conta.sacar_dinheiro(10500)  # utilizando sacar dinheiro

print('Saldo Final')
conta.consultar_saldo()  # utilizando metodo consultar
conta.consulta_limite_chequeespecial()  # utilizando limite chequeespecial
print('--' * 20)
conta.consultar_historico_transacoes()  # utilizando historico de transação


