from ContasBancos import ContaCorrente, CartaoCredito

#  programa
conta = ContaCorrente("Daniel", "111.111.111-00", 123456, 34062)

cartao = CartaoCredito("Daniel", conta)

conta.nome = 'Daniel Carmo'
print(conta.nome)

cartao.senha = '12223'
print(cartao.senha)

# __dict__  é um dicionário que contém todos os atributos de um objeto, incluindo métodos e variáveis de instância.
print(conta.__dict__)
print(cartao.__dict__)

# print(cartao.conta_corrente._num_conta)

#print(cartao.numero)
#print(cartao.cod_seguranca)
#print(cartao.validade)

# depositando dinheiro
#conta.deposita(10000)  # utilizando metodo depositar
#conta.consultar_saldo()  # utilizando metodo consultar

#  sacando dinheir
#  conta.sacar_dinheiro(10500)  # utilizando sacar dinheiro

#print('Saldo Final')
#conta.consultar_saldo()  # utilizando metodo consultar
#conta.consulta_limite_chequeespecial()  # utilizando limite chequeespecial

#print('--' * 20)
#conta.consultar_historico_transacoes()  # utilizando historico de transação

#print('--' * 20)
#conta_2 = ContaCorrente('Fulano', "222-222-222-22", 564445, 44444)
#conta.transferir(850, conta_2) # utilizzando o meto de tranferir para outra conta

#print('--' * 20)
#conta.consultar_saldo()

#print('--' * 20)
#conta_2.consultar_saldo()

#print('--' * 20)
#conta.consultar_historico_transacoes()

#print('--' * 20)
#conta_2.consultar_historico_transacoes()

#help(ContaCorrente)  # 0exibe informações sobre a classe.