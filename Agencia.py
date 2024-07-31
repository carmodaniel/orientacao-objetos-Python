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
class AgenciaCcomun(Agencia):
    pass


class AgenciaVirtual(Agencia):
    pass


class AgenciaPremium(Agencia):
    pass



agencia_primeira = Agencia(123456789, 122222122212221, 11111)

agencia_primeira.caixa = 1000000

agencia_primeira.verificar_caixa()

agencia_primeira.emprestar_dinheiro(1500, 123456666444, 0.2)
print(agencia_primeira.emprestimos)


agencia_primeira.adicionar_cliente('Daniel', 11111111, 100000)
print((agencia_primeira.clientes))


