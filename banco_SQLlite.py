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
            STATUS_PAGAMENTO TEXT DEFAULT 'pendente',
            TELEFONE TEXT
        )                            
        ''')
        self.conn.commit()
    
    def criar_usuarios(self, nome,cpf,data_nascimento,valor_divida,telefone):
        self.cursor.execute(
        'INSERT INTO clientes_inadimplentes (nome,cpf,data_nascimento,valor_divida,telefone) VALUES (?,?,?,?,?)',
        (nome,cpf,data_nascimento,valor_divida,telefone)

        )
        self.conn.commit()
