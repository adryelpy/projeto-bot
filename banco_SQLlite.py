import sqlite3

class MeuBanco:
    def __init__(self):
        self.conn = sqlite3.connect('banco_bot')
        self.cursor = self.conn.cursor()
    
    def criar_tabelas(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes_inadimplentes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            NOME TEXT,
            CPF TEXT,
            DATA_NASCIMENTO DATE,
            VALOR_DIVIDA REAL,
            TELEFONE TEXT,
            STATUS_CLIENT TEXT DEFAULT 'pendente'
        )                            
        ''')
        self.conn.commit()
    
    def criar_usuarios(self, nome,cpf,data_nascimento,valor_divida,telefone,status_client):
        self.cursor.execute(
        'INSERT INTO clientes_inadimplentes (nome,cpf,data_nascimento,valor_divida,telefone,status_client) VALUES (?,?,?,?,?,?)',
        (nome,cpf,data_nascimento,valor_divida,telefone,status_client)

        )
        self.conn.commit()

                       
    def consulta_status(self,status_client):
        self.cursor.execute(
            'SELECT TELEFONE FROM clientes_inadimplentes WHERE STATUS_CLIENT = ?',
            (status_client,)
        )
        resultados = self.cursor.fetchall() # pega todos os resultados e transforma em uma lista de tuplas
        return resultados                   # aqui estamos retornando esta lista de tuplas

