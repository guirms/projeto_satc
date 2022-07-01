import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="1234567",
  database="bancoprojetopython"
)

mycursor = mydb.cursor()

# mycursor.execute("insert into Reserva(nomePessoaTitular, cpf, numeroPessoas, tipoQuarto, numeroDias, valor, statusQuarto) values('josao', '12746462940', 2, 'D', 1, 13.0, 'R')")
# sql = ("INSERT INTO reserva(nomePessoaTitular, cpf, numeroPessoas, tipoQuarto, numeroDias, valor, statusQuarto)"
#            " values(%s, %s, %s, %s, %s, %s, %s)")
# values = ('aev', '123', 2, 's', 2, 3, 'r')
# mycursor.execute(sql, values)
# mycursor.execute("SELECT * FROM reserva where cpf='123' and statusQuarto='R'")
# row = mycursor.fetchone()
#
# while row is not None:
#     print(row)
#     row = mycursor.fetchone()
#

# mycursor.execute(f"UPDATE reserva SET statusQuarto = 'R' where cpf='123'")
# mydb.commit()

mycursor.execute("SELECT * FROM reserva")
row = mycursor.fetchone()
while row is not None:
     print(row)
     row = mycursor.fetchone()