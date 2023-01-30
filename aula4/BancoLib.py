import random
import sqlite3


class Banco():
    def __init__(self, nome):
        self.nome = nome
        conn = sqlite3.connect('banco_ufrpe.db')
        cursor = conn.cursor()
        cursor.execute(
            '''CREATE TABLE BANCO (ID INTEGER PRIMARY KEY, NOME TEXT)''')
        cursor.execute(
            '''CREATE TABLE CONTAS (ID INTEGER PRIMARY KEY, SALDO FLOAT)''')
        cursor.commit()
        cursor.execute(f'INSERT INTO BANCO (ID, NOME) VALUES (1, {nome})')

        # valores = {"ID": 1, "NOME": nome}
        # cursor.execute(
        #     "INSERT INTO BANCO(ID, NOME) VALUES (:ID, :NOME)", valores)
        cursor.commit()
        self.conn = conn
        self.cursor = cursor

    def getNome(self):
        return self.nome

    def criarConta(self):
        num = random.randint(0, 1000)
        cursorLocal = self.cursor
        cursorLocal.execute(f'INSERT INTO CONTA (ID, SALDO) VALUES ({num}, 0)')
        cursorLocal.commit()
        # c = Conta(num)
        # self.contas.append(c)
        return num

    def consultaSaldo(self, numConta):
        cursorLocal = self.cursor
        cursorLocal.execute(f'SELECT SALDO FROM CONTA WHERE ID == {numConta}')
        result = cursorLocal.fetchone()
        if (result):
            return result[0]
        else:
            return -1

    def depositar(self, numConta, valor):
        cursorLocal = self.cursor
        cursorLocal.execute(
            f'SELECT SALDO CONTA WHERE ID == {numConta}')
        result = cursorLocal.fetchone()
        if (result):
            novoSaldo = result[0] + valor
            cursorLocal.execute(
                f'UPDATE CONTA SET SALDO = {novoSaldo} WHERE ID == {numConta}')
            result = cursorLocal.commit()
        else:
            return -1

    def sacar(self, numConta, valor):
        for conta in self.contas:
            if conta.numero == numConta:
                return conta.sacar(valor)

    def closeAll(self):
        self.cursor.close()
        self.conn.close()
