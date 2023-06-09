import mysql.connector

## La forma en la que nos conectaremos a nuestra database ##
mydb = mysql.connector.connect(
    host="localhost",  # Para todos asi
    user="Eli",  # Unico segun como se registraron el Workbench
    password="Resident-1",
    database="Curso_Python"
)

mycursor = mydb.cursor()

## Crear una database con el nombre escogido ##

# mycursor.execute("CREATE DATABASE Curso_Python")

## Visualizar todas las database que se tienen existentes ##

# mycursor.execute("SHOW DATABASES")
#
# for x in mycursor:
#     print(x)

## Acceder a una database y crear una tabla dentro de ella ##

# mycursor.execute("CREATE TABLE Prueba_2 (name VARCHAR(255), address VARCHAR(255), city VARCHAR(255), country VARCHAR(255))")

## Revisar que tablas existen ##

# mycursor.execute("SHOW TABLES")
#
# for x in mycursor:
#   print(x)

## Agregar clase id en tabla nueva

# mycursor.execute("CREATE TABLE Prueba_3 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

## Alterar tabla ya existente

# mycursor.execute("ALTER TABLE Prueba_2 ADD COLUMN number INT ")

## Agregar valores a la tabla

# sql = "INSERT INTO Prueba_1 (name , address) VALUES (%s, %s)"
# val = ("David", "Lowway 24")
# mycursor.execute(sql, val)
#
# mydb.commit()
#
# print(mycursor.rowcount, "record inserted.")

##Multiples Valores

# sql = "INSERT INTO Prueba_1 (name, address) VALUES (%s, %s) "
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]
#
# mycursor.executemany(sql, val)
#
# mydb.commit()
#
# print(mycursor.rowcount, "was inserted.")

## Conseguir el ultimo ID

# sql = "INSERT INTO Prueba_1 (name, address) VALUES (%s, %s)"
# val = ("Michelle", "Blue Village")
# mycursor.execute(sql, val)
#
# mydb.commit()
#
# print("1 record inserted, ID:", mycursor.lastrowid)

## Seleccionar una tabla

# mycursor.execute("SELECT * FROM Prueba_1")
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#     print(x)

## Seleccionar una columna de una tabla

# mycursor.execute("SELECT name, address FROM Prueba_1")
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)

## Selecciona solo una fila

# mycursor.execute("SELECT * FROM Prueba_1")
#
# myresult = mycursor.fetchone()
#
# print(myresult)

## WHERE

# sql = "SELECT * FROM Prueba_1 WHERE name LIKE '%way%'"
#
# mycursor.execute(sql)
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)

##  ORDER BY

# sql = "SELECT * FROM Prueba_1 ORDER BY address DESC"
#
# mycursor.execute(sql)
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)

## UPDATE

# sql = "UPDATE Prueba_1 SET address = %s WHERE address = %s"
# val = ("Canyon 123", "Valley 345")
#
# mycursor.execute(sql, val)
#
# mydb.commit()
#
# print(mycursor.rowcount, "record(s) affected")

