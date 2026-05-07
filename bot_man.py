# instanciando o banco de dados
from banco_SQLlite import MeuBanco 
from datetime import datetime

bancobot = MeuBanco()
bancobot.criar_tabelas()

nome = input('nome do cliente:\n')
cpf = input('CPF do cliente:\n')
data_nascimento = input('dada de nascimento do cliente:\n')
data_objeto = datetime.strptime(data_nascimento, "%d/%m/%Y")
valor_divida = float(input(f'Valor da divida do cliente:\n'))
telefone = input('Telefone para contato do cliente:\n')
bancobot.criar_usuarios(nome,cpf,data_nascimento,valor_divida,telefone)



