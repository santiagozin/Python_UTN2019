#!/usr/bin/env python
# -*- coding: utf-8 -*-
# AGT
# Copyright 2019 Ariel H Garcia Traba <ariel.garcia.traba@gmail.com>
#
print("############################################################################");
print("##                                                                        ##");
print("##      Unidad 1 -¿Qué es Python?                                         ##");
print("##            * Instalación y configuración                               ##");
print("##            * Errores sintácticos y lógicos                             ##");
print("##            * Programación secuencial                                   ##");
print("##            * Estructuras condicionales simples, compuestas y anidadas  ##");
print("##            * Estructuras repetitivas                                   ##");
print("##                                                                        ##");
print("##      Unidad 2 - Variables, Listas                                      ##");
print("##            * Tipos de variables                                        ##");
print("##            * Procesamiento de cadenas                                  ##");
print("##            * Listas                                                    ##");
print("##            * Diccionarios                                              ##");
print("##                                                                        ##");
print("##      Unidad 3 - Funciones                                              ##");
print("##            * Parámetros                                                ##");
print("##            * Retorno de datos                                          ##");
print("##            * Return de listas                                          ##");
print("##            * Parámetros con valor por defecto                          ##");
print("##                                                                        ##");
print("##      Unidad 4 - Listas, Tuplas y Diccionarios                          ##");
print("##         Listas                                                         ##");
print("##            * Índices                                                   ##");
print("##            * Recorrer listas                                           ##");
print("##         Tuplas                                                         ##");
print("##            * Índices                                                   ##");
print("##            * Recorrer Tuplas                                           ##");
print("##         Diccionarios                                                   ##");
print("##            * Funcionamiento de diccionarios                            ##");
print("##            * Estructuras tipo JSON                                     ##");
print("##                                                                        ##");
print("##         Unidad 5 - MySQL, Parte 1                                      ##");
print("##            * INSERT, UPDATE, DELETE, SELECT                            ##");
print("##            * FECHAS Y HORAS                                            ##");
print("##            * %LIKE%                                                    ##");
print("##            * JOIN                                                      ##");
print("##                                                                        ##");
print("##         Unidad 6 - MySQL, Parte 2                                      ##");
print("##            * MySQL en Python                                           ##");
print("##            * Cursor y verificación de consultas                        ##");
print("##            * Manejo de errores                                         ##");
print("##                                                                        ##");
print("##         Unidad 7 - Fechas, Horas, Archivos                             ##");
print("##            * Modulo time, datetime                                     ##");
print("##            * Manejo de fechas y horas                                  ##");
print("##            * Operaciones con archivos                                  ##");
print("##                                                                        ##");
print("##         Unidad 8 - OPEN CV                                             ##");
print("##            * Procesamiento de imágenes en OpenCV                       ##");
print("##            * Detección y descripción de imágenes                       ##");
print("##            * Detección de objetos                                      ##");
print("##                                                                        ##");
print("##         Unidad 9 - Programación de eventos                             ##");
print("##            * Módulo sched                                              ##");
print("##            * Declaración de programadores                              ##");
print("##            * Programar eventos y poner en marcha el programador        ##");
print("##            * Programación de eventos considerando prioridades          ##");
print("##            * Cancelación de eventos                                    ##");
print("##                                                                        ##");
print("##         Unidad 10 - GIT Colaborativo -Pair Programming                 ##");
print("##            * Introducción a CVS y comparativa con SVN                  ##");
print("##            * Creando un repositorio con GIT, clonar, crear branches    ##");
print("##            * Borrar, guardar (stash), recuperar (pop)                  ##");
print("##            * Configuración de remote                                   ##");
print("##            * Configuración de Git avanzada                             ##");
print("##                                                                        ##");
print("############################################################################");
print("##                                                                        ##");
print("##         Unidad 5 - MySQL, Parte 1                                      ##");
print("##            * INSERT, UPDATE, DELETE, SELECT                            ##");
print("##            * FECHAS Y HORAS                                            ##");
print("##            * %LIKE%                                                    ##");
print("##            * JOIN                                                      ##");
print("##                                                                        ##");
print("##         Unidad 6 - MySQL, Parte 2                                      ##");
print("##            * MySQL en Python                                           ##");
print("##            * Cursor y verificación de consultas                        ##");
print("##                                                                        ##");
print("############################################################################");
print("##                                                                        ##");
print("##                              Bases de Datos                            ##");
print("##                                                                        ##");
print("##                         libreria mysql.connector                       ##");
print("##                                                                        ##");
print("############################################################################");
print("##                                                                        ##");
print("##                         Create Database                                ##");
print("##                         Create Table                                   ##");
print("##                         Insert                                         ##");
print("##                         Select                                         ##");
print("##                         Where                                          ##");
print("##                         Order By                                       ##");
print("##                         Delete                                         ##");
print("##                         Drop Table                                     ##");
print("##                         Update                                         ##");
print("##                         Limit                                          ##");
print("##                         Join                                           ##");
print("##                                                                        ##");
print("############################################################################");
print("##                                                                        ##");
print("##                MySQL has 3 main categories of data types namely        ##");
print("##                                                                        ##");
print("##                               Numeric,                                 ##");
print("##                               Text                                     ##");
print("##                               Date/time.                               ##");
print("##                                                                        ##");
print("##  Numeric Data types                                                    ##");
print("##  Numeric data types are used to store numeric values. It is very       ##");
print("##    important to make sure range of your data is between lower and upper##");
print("##    boundaries of numeric data types.                                   ##");
print("##               TINYINT( )    -128 to 127 normal 0 to 255                ##");
print("##               SMALLINT( )   -32768 to 32767 normal                     ##");
print("##               MEDIUMINT( )  -8388608 to 8388607 normal                 ##");
print("##               INT( )        -2147483648 to 2147483647 normal           ##");
print("##               BIGINT( )     -9223372036854775808 to                    ##");
print("##                           9223372036854775807 normal                   ##");
print("##               FLOAT         A small approximate number with a floating ##");
print("##                   decimal point.                                       ##");
print("##               DOUBLE( , )   A large number with a floating decimal     ##");
print("##                   point.                                               ##");
print("##               DECIMAL( , )  A DOUBLE stored as a string , allowing     ##");
print("##                   for a fixed decimal point. Choice for storing        ##");
print("##                   currency values.                                     ##");
print("##                                                                        ##");
print("##  Text Data Types                                                       ##");
print("##  As data type category name implies these are used to store text values##");
print("##  Always make sure you length of your textual data do not exceed        ##"); 
print("##  maximum lengths.                                                      ##");
print("##               CHAR( )       A fixed section from 0 to 255 characters   ##");
print("##               VARCHAR( )    A variable section from 0 to 255 chrs      ##");
print("##               TINYTEXT      A string with a max. length of 255 chrs.   ##");
print("##               TEXT          A string with a max. length of 65535       ##");
print("##               BLOB          A string with a max. length of 65535       ##");
print("##               MEDIUMTEXT    A string with a max. length of 16777215    ##");
print("##               MEDIUMBLOB    A string with a max. length of 16777215    ##");
print("##               LONGTEXT      A string with a max. length of 4294967295  ##");
print("##               LONGBLOB      A string with a max. length of 4294967295  ##");
print("##                                                                        ##");
print("##  Date / Time                                                           ##");
print("##               DATE          YYYY-MM-DD                                 ##");
print("##               DATETIME      YYYY-MM-DD HH:MM:SS                        ##");
print("##               TIMESTAMP     YYYYMMDDHHMMSS                             ##");
print("##               TIME          HH:MM:SS                                   ##");
print("##                                                                        ##");
print("############################################################################");
print("##                                                                        ##");
print("##  Apart from above there are some other data types in MySQL.            ##");
print("##                                                                        ##");
print("##  ENUM     To store text value chosen from a list of predefined text    ##");
print("##           values                                                       ##");
print("##  SET      This is also used for storing text values chosen from a list ##");
print("##           predefined text values. It can have multiple values.         ##");
print("##  BOOL     Synonym for TINYINT(1), used to store Boolean values         ##");
print("##  BINARY   Similar to CHAR, difference is texts are stored in binary    ##");
print("##           format.                                                      ##");
print("##  VARBINARY   Similar to VARCHAR, difference is texts are stored        ##");
print("##              in binary format.                                         ##");
print("##                                                                        ##");
print("############################################################################");

def limpiar():
    import os
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
print("Inicio ej015_1 -  ");
print("#########################################################");
print (r" C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>python -m pip install mysql-connector ");
print("https://www.w3schools.com/python/python_mysql_create_db.asp")
import mysql.connector
def Iniciar_practica():
	try:
		print ("Conectamos con MySQL")
		conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019")#database='nombre',
		puntero = conectarse.cursor()
		accion = input ("Drop la DDBB (S/N)")
		if accion.upper() == "S":
			puntero.execute("DROP DATABASE UTN_practica1_2019")
		puntero.execute("CREATE DATABASE UTN_practica1_2019")
		print ("Creamos la base de datos  UTN_practica1_2019")
		puntero.close
		conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019", database="UTN_practica1_2019")
		puntero = conectarse.cursor()
		puntero.execute("CREATE TABLE 2019_Marzo (id INT AUTO_INCREMENT PRIMARY KEY, ALUMNO_APELLIDO VARCHAR(255), ALUMNO_NOMBRE VARCHAR(255), ALUMNO_MAIL VARCHAR(255), ALUMNO_CELULAR VARCHAR(255), ALUMNO_EDAD INT)")
		puntero.execute("SHOW TABLES")
		print ("Mostramos las tablas de la bases de datos UTN_practica1_2019")
		lista_de_tablas=[]
		for lista_tablas in (puntero):
			lista_nombres_tablas=str(lista_tablas)
			lista_nombres_tablas_largo=len(lista_tablas)-4
			lista_nombres_tablas=lista_nombres_tablas[2:lista_nombres_tablas_largo]
			print ("*"+lista_nombres_tablas+"*")
			lista_de_tablas.append(lista_nombres_tablas);
		print (lista_de_tablas)
		columnas_mysql = "INSERT INTO 2019_Marzo (ALUMNO_APELLIDO, ALUMNO_NOMBRE, ALUMNO_MAIL, ALUMNO_CELULAR, ALUMNO_EDAD)  VALUES (%s, %s, %s, %s, %s)"
		datos = ("Garcia Traba", "Ariel" , "ariel.garcia.traba@gmail.com","+5491144754637","45")
		puntero.execute(columnas_mysql, datos)
		conectarse.commit()
		print(puntero.rowcount, "record inserted.")
		puntero.close
	except Exception as e:
		print("Exeception occured:{}".format(e))
	finally:
		conectarse.close()
def crear_base():
	try:
		nombre_DDBB = input("ingrese el nombre de la base de datos a crear : ")
		nombre_DDBB = nombre_DDBB.capitalize()
		print ("Conectamos con MySQL")
		conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019")#database='nombre',
		puntero = conectarse.cursor()
		puntero.execute("CREATE DATABASE "+str(nombre_DDBB))
		print ("Creamos la base de datos  "+str(nombre_DDBB))
		print ("cerramos coneccion")
		puntero.close
	except Exception as e:
		print("Exeception occured:{}".format(e))
	finally:
		conectarse.close()
def listar_bases():
	try:
		print ("Conectamos con MySQL")
		conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019")
		puntero = conectarse.cursor()
		puntero.execute("SHOW DATABASES")
		print ("Mostramos las bases de datos  ")
		lista_de_bases=[]
		for lista_bases in (puntero):
			lista_nombres_bases=str(lista_bases)
			lista_nombres_bases_largo=len(lista_bases)-4
			lista_nombres_bases=lista_nombres_bases[2:lista_nombres_bases_largo]
			print ("*"+lista_nombres_bases+"*")
			lista_de_bases.append(lista_nombres_bases);
		print (lista_de_bases)
		print ("cerramos coneccion")
		puntero.close
	except Exception as e:
		print("Exeception occured:{}".format(e))
	finally:
		conectarse.close()
def crear_tablas():
	try:
		nombre_DDBB = input("ingrese el nombre de la base de datos para insertar tablas : ")
		nombre_DDBB = nombre_DDBB.capitalize()
		nombre_tabla = input("ingrese el nombre de la nombre tabla a crear : ")
		nombre_tabla = nombre_tabla.upper()
		nombre_columna_1 = input("ingrese el nombre de la nombre_columna_1 a crear : ")
		nombre_columna_1 = nombre_columna_1.upper()
		nombre_columna_2 = input("ingrese el nombre de la nombre_columna_1 a crear : ")
		nombre_columna_2 = nombre_columna_2.upper()
		nombre_columna_3 = input("ingrese el nombre de la nombre_columna_1 a crear : ")
		nombre_columna_3 = nombre_columna_3.upper()
		
		print ("Conectamos con MySQL")
		conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019",database=str(nombre_DDBB))
		puntero = conectarse.cursor()
		puntero.execute("USE "+str(nombre_DDBB)); # select the database
		puntero.execute("SHOW TABLES")    # execute 'SHOW TABLES' (but data is not returned)
		tablas = puntero.fetchall()       # return data from last query
		print (tablas)
		puntero.execute("CREATE TABLE "+str(nombre_tabla)+" (id INT AUTO_INCREMENT PRIMARY KEY, "+str(nombre_columna_1)+" VARCHAR(255), "+str(nombre_columna_2)+" INT, "+str(nombre_columna_3)+" VARCHAR(255))")
		print ("cerramos coneccion")
		puntero.close
	except Exception as e:
		print("Exeception occured:{}".format(e))
	finally:
		conectarse.close()
def agregar_id_tablas():
	try:
		nombre_DDBB = input("ingrese el nombre de la base de datos para insertar tablas : ")
		nombre_DDBB = nombre_DDBB.capitalize()
		print ("Conectamos con MySQL")
		conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019",database=str(nombre_DDBB))
		puntero = conectarse.cursor()
		puntero.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") 
		print (lista_de_tablas)
		print("cerramos coneccion");
		puntero.close
	except Exception as e:
		print("Exeception occured:{}".format(e))
	finally:
		conectarse.close()	
def listar_tablas():
	try:
		nombre_DDBB = "UTN_practica1_2019";
	#	nombre_DDBB = input("ingrese el nombre de la base de datos para insertar tablas : ")
	#	nombre_DDBB = nombre_DDBB.capitalize()
		print ("Conectamos con MySQL")
		conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019",database=str(nombre_DDBB))
		puntero = conectarse.cursor()
		puntero.execute("SHOW TABLES")
		print ("Mostramos las tablas de la bases de datos "+str(nombre_DDBB))
		lista_de_tablas=[]
		for lista_tablas in (puntero):
			lista_nombres_tablas=str(lista_tablas)
			lista_nombres_tablas_largo=len(lista_tablas)-4
			lista_nombres_tablas=lista_nombres_tablas[2:lista_nombres_tablas_largo]
			print ("*"+lista_nombres_tablas+"*")
			lista_de_tablas.append(lista_nombres_tablas);
		print (lista_de_tablas)
		colunma_numero = int(input("Ingrese el numero de la tabla cuyas columnas desea listar : "));
	#	for columnas in  lista_de_tablas
		puntero.execute("SHOW columns FROM "+str(lista_de_tablas[colunma_numero]))
		for column in puntero.fetchall():
			print (column[colunma_numero]);
		print("cerramos coneccion");
		puntero.close
	except Exception as e:
		print("Exeception occured:{}".format(e))
	finally:
		conectarse.close()
def agregar_datos_tablas():
	try:
		print ("Conectamos con MySQL")
		conectarse = mysql.connector.connect(host="localhost",user="root", passwd="mysql2019", database="UTN_practica1_2019")
		puntero = conectarse.cursor()
		puntero.execute("SHOW TABLES")
		print ("Mostramos las tablas de la bases de datos UTN_practica1_2019")
		lista_de_tablas=[]
		for lista_tablas in (puntero):
			lista_nombres_tablas=str(lista_tablas)
			lista_nombres_tablas_largo=len(lista_tablas)-4
			lista_nombres_tablas=lista_nombres_tablas[2:lista_nombres_tablas_largo]
			print ("*"+lista_nombres_tablas+"*")
			lista_de_tablas.append(lista_nombres_tablas);
		print (lista_de_tablas)
		columnas_mysql = "INSERT INTO 2019_Marzo (ALUMNO_APELLIDO, ALUMNO_NOMBRE, ALUMNO_MAIL, ALUMNO_CELULAR, ALUMNO_EDAD)  VALUES (%s, %s, %s, %s, %s)"
		ALUMNO_APELLIDO = str(input("Ingrese su apellido : "));
		ALUMNO_NOMBRE = str(input("Ingrese su nombre : "));
		ALUMNO_MAIL = str(input("Ingrese su Email : "));
		ALUMNO_CELULAR = str(input("Ingrese su celular : "));
		ALUMNO_EDAD = str(input("Ingrese su edad : "));
		datos = (ALUMNO_APELLIDO, ALUMNO_NOMBRE, ALUMNO_MAIL, ALUMNO_CELULAR, ALUMNO_EDAD)
		puntero.execute(columnas_mysql, datos)
		conectarse.commit()
		print(puntero.rowcount, "record inserted.")
		puntero.close
	except Exception as e:
		print("Exeception occured:{}".format(e))
	finally:
		conectarse.close()
		
accion = input ("Creamos base de datos (S/N)");
if accion.upper() =="S": crear_base();
accion= input("Listamos base de datos existentes (S/N)");
if accion.upper() =="S": listar_bases();
accion = input ("Creamos Tablas en la base de datos (S/N)");
if accion.upper() =="S": crear_tablas();
accion= input("Agrego collumna ID en tabla existentes (S/N)");
if accion.upper() =="S": agregar_id_tablas();	
accion= input("Inicio practica alumnos (S/N)");
if accion.upper() =="S": Iniciar_practica()
accion= input("Listamos Tablas en la base de datos UTN_practica1_2019 (S/N)");
if accion.upper() =="S": listar_tablas();
accion= input("Agregar datos en la base de datos UTN_practica1_2019 (S/N)");
if accion.upper() =="S": agregar_datos_tablas();

'''















import datetime
import mysql.connector
 
connection = mysql.connector.connect(user='user', password='password', database='database')
cursor = connection.cursor()
 
dni = 10
nombre = 'George'
apellido = 'Lopez'
fecha_nacimiento = datetime.date(1961, 4, 23)
lugar_nacimiento = 'Mission Hills, California, Estados Unidos'
domicilio = 'California'
e_mail = 'george@lopez.com'
 
sql = """
	INSERT INTO alumno
	(
		dni,
		nombre,
		apellido,
		fecha_nacimiento,
		lugar_nacimiento,
		domicilio,
		e-mail
	)
	VALUES (
		%s,
		%s,
		%s,
		%s,
		%s,
		%s,
		%s,
		)
	"""
datos = (dni, nombre, apellido, fecha_nacimiento, lugar_nacimiento, domicilio, e_mail)
cursor.execute(sql, datos)
cursor.commit()
 
cursor.close()
connection.close()
'''
