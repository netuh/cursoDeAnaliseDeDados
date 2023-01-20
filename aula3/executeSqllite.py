import sqlite3

con = sqlite3.connect("bancoDeDados.db")

cursor = con.cursor()

cursor.execute(
    '''DROP TABLE ALUNO''')
con.commit()

cursor.execute(
    '''CREATE TABLE ALUNO (MATRICULA INTEGER,
        SENHA VARCHAR(30), CPF INT, NOME VARCHAR(20))''')
con.commit()

cursor.execute("INSERT INTO ALUNO VALUES (10, 'TESTE', 1, 'Neto')")
cursor.execute("INSERT INTO ALUNO VALUES (20, 'TESTE', 2, 'Waldemar')")
cursor.execute("INSERT INTO ALUNO (MATRICULA, NOME) VALUES (11, 'Pires')")
con.commit()

cursor.execute("DELETE FROM ALUNO WHERE MATRICULA = 11")
con.commit()

login = input("digite seu nome:")
senha = input("digite sua senha:")
items = {"login": login, "senha": senha}

cursor.execute(
    "SELECT * FROM ALUNO WHERE NOME = :login AND SENHA = :senha", items)
result = cursor.fetchone()
print(result)
if result:
    print("voce esta logado")
    print(result[3])
else:
    print("Login e senha errados")

# result = cursor.fetchmany(5)
# print(result)
# for a in result:
#     print(a)

cursor.close()
con.close()
