# """
#Avaliação – Python + SQLite
#Tema: CRUD em 'alunos'

#O que o script deve fazer:
#1) Criar 'escola.db'
#2) Criar tabela 'alunos' -> Seguindo o diagrama
#3) Inserir registros na tabela alunos
#4) Listar todos
#5) Buscar por id
#6) Atualizar registros
#7) Deletar registros

#"""

import sqlite3 
conn= sqlite3.connect('escola.db') #db=database
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS alunos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    email TEXT 
    )''')

print('Tabela criada com sucesso!')
cursor.execute('INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)', ('Isa', 18, 'isa@gmail.com'))
cursor.execute('INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)', ('Rosa', 17, 'rosaa@gmail.com'))
cursor.execute('INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)', ('Nala', 19, 'nala@gmail.com'))
cursor.execute('INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)', ('Luise', 16, 'lulu@gmail.com'))
conn.commit()
print('Dados adicionados com sucesso!')

print('Lista de alunos:')
cursor.execute('SELECT * FROM alunos')

for linha in cursor.fetchall():
    print(linha)
print()

cursor.execute('UPDATE alunos SET email = ? WHERE nome = ?',('roses@gmail.com', 'Rosa'))
conn.commit()
print('Email Atualizado!')
cursor.execute('SELECT * FROM alunos')
for linha in cursor.fetchall():
    print(linha)
print()

cursor.execute('DELETE FROM alunos WHERE id = ?', (1,))

conn.commit()
print('ID deletado!')
cursor.execute('SELECT * FROM alunos')
for linha in cursor.fetchall():
    print(linha)
print()

conn.close()

