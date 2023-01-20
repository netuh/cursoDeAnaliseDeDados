import sqlite3

con = sqlite3.connect("bancoDeDados.db")

cursor = con.cursor()

cursor.execute(
    '''DROP TABLE ALUNO''')
con.commit()

cursor.execute(
    '''CREATE TABLE ALUNO (MATRICULA INTEGER, CPF INT, NOME VARCHAR(20))''')
con.commit()


cursor.execute("INSERT INTO ALUNO VALUES (10, 1, 'Neto')")
cursor.execute("INSERT INTO ALUNO VALUES (20, 2, 'Waldemar')")
cursor.execute("INSERT INTO ALUNO (MATRICULA, NOME) VALUES (11, 'Pires')")
con.commit()

cursor.execute("DELETE FROM ALUNO WHERE MATRICULA = 11")
con.commit()

cursor.execute("SELECT NOME FROM ALUNO ")
result = cursor.fetchmany(5)
print(result)
# for a in result:
#     print(a)

cursor.close()
con.close()
