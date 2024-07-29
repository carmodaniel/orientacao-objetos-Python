# Orientação a objetos
from datetime import datetime # biblioteca para pegar data e hora
import pytz # biblioteca para formatação de suso
from random import randint


# criação da classe
class ContaCorrente:
    """
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes.

    Atributos:
        nome (str): Nome do cliente.
        cpf (str): CPF do clinete, deve ser inserido com pontos e traço.
        saldo: saldo disponível da conta do cliente
        limite: Limite de cheque especial do cliente
        agencia: Agencia da conta do cliente
        num_conta: Número da conta do cliente
        transacoes: Histórico de transações do cliente
    """

    @staticmethod  # O @staticmethod em Python é um decorador usado para definir um método estático dentro de uma classe. Vamos entender o que isso significa:
    def _data_hora():  # Um método estático é uma função que pertence à classe, mas não depende de instâncias específicas (objetos) dessa classe
        fuso_br = pytz.timezone('Brazil/East') #  utilzando pytz.timezone para pegar timezone do brasil
        horario_br = datetime.now(fuso_br)
        return horario_br.strftime('%d/%m/%Y %H:%M:%S') # utilzando strftime para formatar data e hora em dia/mes/Ano Hora:Minuto:Segundo

    def __init__(self, nome, cpf, agencia, num_conta):  # O método __init__ é chamado quando um objeto é criado. Ele inicializa os atributos da instância.
        self.nome = nome
        self.cpf = cpf
        self._saldo = 0
        self._limite = None
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []
        self.cartoes = []

    # Criação de metodos
    def consultar_saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self._saldo))

    def deposita(self, valor):  # metodo depositar
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):  # metodo limite conta interno para ser urtilizado dentro da classe
        self._limite = -1000
        return self._limite

    def sacar_dinheiro(self, valor):  # metodo sacar
        if self._saldo - valor < self._limite_conta():  # utilizando o metodo limite_conta para validar limite
            print("Você não tem Saldo suficiente para sacar esse valor")
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))

    def consulta_limite_chequeespecial(self):  # metodo consulta cheque especial
        print('Seu límite de cheque especial é de R${:,.2f}'.format(
            self._limite_conta()))

    def consultar_historico_transacoes(self):  # metodo para historico de transação
        print('Histórico de Transaç es')
        print('Valor, Saldo, Data e Hora')
        for transacao in self._transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino): # metodo transferir para utilizar  parametro de conta para transferir
        if self._saldo - valor < self._limite_conta():  # utilizando o metodo limite_conta para validar limite
            print("Você não tem Saldo suficiente para transferir")
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
            conta_destino._saldo += valor
            conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))

class CartaoCredito:

    @staticmethod  # O @staticmethod em Python é um decorador usado para definir um método estático dentro de uma classe. Vamos entender o que isso significa:
    def _data_hora():  # Um método estático é uma função que pertence à classe, mas não depende de instâncias específicas (objetos) dessa classe
        fuso_br = pytz.timezone('Brazil/East')  # utilzando pytz.timezone para pegar timezone do brasil
        horario_br = datetime.now(fuso_br)
        return horario_br

    def __init__(self, titula, conta_corrente):
        self.numero = randint(1000000000000000,9999999999999999)
        self.titular = titula
        self.validade ='{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year+4)
        self.cod_seguranca = '{}{}{}'.format(randint(0,9), randint(0,9), randint(0,9))
        self.limite = 1000
        self._senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor):
        if len(valor) ==4 and valor.isnumeric():
            self._senha = valor
        else:
            print("Nova senha errada")