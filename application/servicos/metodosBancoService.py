import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="1234567",
  database="bancoprojetopython"
)

mycursor = mydb.cursor()

def inserir(valores):
    sql = ("INSERT INTO reserva(nomePessoaTitular, cpf, numeroPessoas, tipoQuarto, numeroDias, valor, statusQuarto)"
           " values(%s, %s, %s, %s, %s, %s, %s)")
    values = valores
    mycursor.execute(sql, values)
    mydb.commit()

def consultarTabela(tabela):
    mycursor.execute(f"SELECT * FROM bancoprojetopython.{tabela}")
    row = mycursor.fetchone()
    while row is not None:
        print(row)
        row = mycursor.fetchone()
    mydb.commit()

def getByCpf(cpf, condicao):
    mycursor.execute(f"SELECT * FROM reserva WHERE cpf={cpf} AND statusQuarto='{condicao}'")
    row = mycursor.fetchone()
    listaReservas = []
    while row is not None:
        if row != None:
            listaReservas.append(row)
        row = mycursor.fetchone()
    mydb.commit()
    return listaReservas

def getAllByCpf(cpf):
    mycursor.execute(f"SELECT * FROM reserva WHERE cpf={cpf}")
    row = mycursor.fetchone()
    listaReservas = []
    while row is not None:
        if row != None:
            listaReservas.append(row)
        row = mycursor.fetchone()
    mydb.commit()
    return listaReservas

def getAllByCpfEStatus(cpf, status):
    mycursor.execute(f"SELECT * FROM reserva WHERE cpf='{cpf}' AND statusQuarto='{status}'")
    row = mycursor.fetchone()
    listaReservas = []
    while row is not None:
        if row != None:
            listaReservas.append(row)
        row = mycursor.fetchone()
    mydb.commit()
    return listaReservas

def setarCheckInOuCheckOut(id, statusQuarto):
    mycursor.execute(f"UPDATE reserva SET statusQuarto = '{statusQuarto}' WHERE id={id}")
    mydb.commit()

def atualizarDados(numPessoas, tipoQuarto, numDias, valor, status, id):
    mycursor.execute(f"UPDATE reserva SET "
                     f"numeroPessoas={numPessoas},"
                     f"tipoQuarto='{tipoQuarto}',"
                     f"numeroDias={numDias},"
                     f"valor={valor},"
                     f"statusQuarto='{status}' "
                     f"WHERE id={id}")
    mydb.commit()