from random import randint


class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do nível recomendado. Caixa Atual {}'.format(self.caixa))
        else:
            print('o Valor do caixa está Ok Caixa Atual {}'.format(self.caixa))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Emprestimo não é possivel. Dinheiro não disponivel no caixa')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


# Criando Subclasses da classe Agencia
class AgenciaComun(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone,cnpj, numero=randint(1001, 9999))
        self.caixa = 1000000


class AgenciaVirtual(Agencia):

    def __init__(self, site, telefone, cnpj): #ciando __init  # criando __init__ da sublclasse
        self.site = site
        super().__init__(telefone, cnpj, 1000) # chamado __init__ da classe principal
        self.caixa = 1000000

class AgenciaPremium(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 10000000


agencia_primeira = Agencia(123456789, 122222122212221, 11111)

agencia_virtual = AgenciaVirtual('www.agencia.virtual.com.br', 222222, 1511111)
agencia_virtual.verificar_caixa()
print(agencia_virtual.site)

agencia_comum = AgenciaComun(222222221, 25555566666)
agencia_comum.verificar_caixa()

agenciacia_premium = AgenciaPremium(33333333555, 66666666555)
agenciacia_premium.verificar_caixa()


