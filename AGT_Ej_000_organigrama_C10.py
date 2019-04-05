#!/usr/bin/env python
# -*- coding: utf-8 -*-
# AGT
# Copyright 2019 Ariel H Garcia Traba <ariel.garcia.traba@gmail.com>
#
print("############################################################################");
print("##                                                                        ##");
print("##      Unidad 1 -¿Qué es Python?                                         ##");
print("##            ● Instalación y configuración                               ##");
print("##            ● Errores sintácticos y lógicos                             ##");
print("##            ● Programación secuencial                                   ##");
print("##            ● Estructuras condicionales simples, compuestas y anidadas  ##");
print("##            ● Estructuras repetitivas                                   ##");
print("##                                                                        ##");
print("##      Unidad 2 - Variables, Listas                                      ##");
print("##            ● Tipos de variables                                        ##");
print("##            ● Procesamiento de cadenas                                  ##");
print("##            ● Listas                                                    ##");
print("##            ● Diccionarios                                              ##");
print("##                                                                        ##");
print("##      Unidad 3 - Funciones                                              ##");
print("##            ● Parámetros                                                ##");
print("##            ● Retorno de datos                                          ##");
print("##            ● Return de listas                                          ##");
print("##            ● Parámetros con valor por defecto                          ##");
print("##                                                                        ##");
print("##      Unidad 4 - Listas, Tuplas y Diccionarios                          ##");
print("##         Listas                                                         ##");
print("##            ● Índices                                                   ##");
print("##            ● Recorrer listas                                           ##");
print("##         Tuplas                                                         ##");
print("##            ● Índices                                                   ##");
print("##            ● Recorrer Tuplas                                           ##");
print("##         Diccionarios                                                   ##");
print("##            ● Funcionamiento de diccionarios                            ##");
print("##            ● Estructuras tipo JSON                                     ##");
print("##                                                                        ##");
print("##         Unidad 5 - MySQL, Parte 1                                      ##");
print("##            ● INSERT, UPDATE, DELETE, SELECT                            ##");
print("##            ● FECHAS Y HORAS                                            ##");
print("##            ● %LIKE%                                                    ##");
print("##            ● JOIN                                                      ##");
print("##                                                                        ##");
print("##         Unidad 6 - MySQL, Parte 2                                      ##");
print("##            ● MySQL en Python                                           ##");
print("##            ● Cursor y verificación de consultas                        ##");
print("##            ● Manejo de errores                                         ##");
print("##                                                                        ##");
print("##         Unidad 7 - Fechas, Horas, Archivos                             ##");
print("##            ● Modulo time, datetime                                     ##");
print("##            ● Manejo de fechas y horas                                  ##");
print("##            ● Operaciones con archivos                                  ##");
print("##                                                                        ##");
print("##         Unidad 8 - OPEN CV                                             ##");
print("##            ● Procesamiento de imágenes en OpenCV                       ##");
print("##            ● Detección y descripción de imágenes                       ##");
print("##            ● Detección de objetos                                      ##");
print("##                                                                        ##");
print("##         Unidad 9 - Programación de eventos                             ##");
print("##            ● Módulo sched                                              ##");
print("##            ● Declaración de programadores                              ##");
print("##            ● Programar eventos y poner en marcha el programador        ##");
print("##            ● Programación de eventos considerando prioridades          ##");
print("##            ● Cancelación de eventos                                    ##");
print("##                                                                        ##");
print("##         Unidad 10 - GIT Colaborativo -Pair Programming                 ##");
print("##            ● Introducción a CVS y comparativa con SVN                  ##");
print("##            ● Creando un repositorio con GIT, clonar, crear branches    ##");
print("##            ● Borrar, guardar (stash), recuperar (pop)                  ##");
print("##            ● Configuración de remote                                   ##");
print("##            ● Configuración de Git avanzada                             ##");
print("##                                                                        ##");
print("############################################################################");
print(input("continuar?"));
limpiar();
print("############################################################################");
print("##                                                                        ##");
print("##         Unidad 10 - GIT Colaborativo -Pair Programming                 ##");
print("##            ● Introducción a CVS y comparativa con SVN                  ##");
print("##            ● Creando un repositorio con GIT, clonar, crear branches    ##");
print("##            ● Borrar, guardar (stash), recuperar (pop)                  ##");
print("##            ● Configuración de remote                                   ##");
print("##            ● Configuración de Git avanzada                             ##");
print("##   https://www.youtube.com/watch?v=SJqANWdRG4I&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=76                                                                     ##");
print("############################################################################");
print("Control de versiones utilizando Subversion");
print("https://plone-spanish-docs.readthedocs.io/es/latest/rcs/subversion.html");
print("https://www.ionos.es/digitalguide/paginas-web/desarrollo-web/git-vs-svn-una-comparativa-del-control-de-versiones/");
print("https://code.tutsplus.com/es/tutorials/how-to-read-and-write-csv-files-in-python--cms-29907");
print("https://juanjoalvarez.net/es/detail/2006/aug/19/introsubversion/");
print("https://www.ionos.es/digitalguide/paginas-web/desarrollo-web/git-vs-svn-una-comparativa-del-control-de-versiones/")
print("""
https://programminghistorian.org/es/lecciones/introduccion-control-versiones-github-desktop

https://github.com/agt1973/UTN2019#utn2019
""")
def limpiar():
    import os
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
print("""Git vs. SVN: ¿cuál es el mejor sistema de control de versiones?
Los llamados sistemas de control de versiones fueron creados con el fin de detectar cambios en los documentos o archivos y se encargan de guardar todas las versiones anteriores, incluyendo el registro de fecha y hora, así como el identificador del usuario de un archivo para que los datos puedan ser recuperados y restaurados en cualquier momento. De esta forma, es posible determinar qué usuario ha realizado cambios en un punto determinado. Los objetivos generales de este tipo de sistemas consisten en coordinar el acceso compartido de varios usuarios a los archivos y permitir el desarrollo simultáneo de varias bifurcaciones o branches.  

Generalmente, los sistemas de control de versiones se utilizan para el desarrollo de software, para aplicaciones de oficina y para gestores de contenido. Dos de los más conocidos son Apache Subversion (SVN) y Git, los cuales pueden ser instalados internamente en el servidor propio o externamente en el servidor de algún proveedor de alojamiento web. El servicio de alojamiento basado en la web para proyectos Git es GitHub, mientras que en  RiouxSVN aloja a Subversion. Proveedores como SourceForge ofrecen alojamiento para ambos sistemas.
SVN: el sucesor CVS de CollabNet
A principios del año 2000, CollabNet empezó a desarrollar el software libre Subversion y publicaría, cuatro años más tarde, su primera versión. Con ello, SVN se unió al modelo CVS (Concurrent Versions System). En 2009, el proyecto se trasladó a la Apache Software Foundation, motivo por el cual es conocido actualmente como Apache Subversion.

SVN se basa en un sistema de control de versiones centralizado. Esto significa que existe un almacén central de datos (el repositorio) accesible a todos los usuarios. Dado que los cambios realizados no pueden ser fusionados entre sí, el sistema evita que dos usuarios puedan editar un mismo archivo al mismo tiempo. El proceso es muy simple, cuando uno de los usuarios accede a un archivo, el sistema lo marca automáticamente como de solo lectura para los demás. Además, Apache Subversion ofrece la posibilidad de descargar y editar directorios individuales sin depender del árbol general de directorios. De esta manera, es posible asignar diferentes permisos de lectura y escritura a los diferentes usuarios. Subversion se caracteriza también porque puede registrar directorios vacíos, renombrados y mudados de sitio sin pérdidas de su historia.

VN vs. Git: una comparación directa
Aunque muchos usuarios se preguntan cuál de los dos programas de control de versiones es mejor, no existe una respuesta general. La elección del sistema de control de versiones más adecuado para uno u otro proyecto dependerá de tus objetivos específicos. Ambos sistemas difieren en su estructura y en el proceso de trabajo resultante. La siguiente tabla resume sus principales diferencias: 
""");
import csv
myData = [["first_name", "second_name", "Grade"],
          ['Alex', 'Brian', 'A'],
          ['Tom', 'Smith', 'B']]
 
myFile = open('example2.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
     
print("Writing complete")
	
import csv
with open('example4.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name', 'Grade']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 
    writer.writeheader()
    writer.writerow({'Grade': 'B', 'first_name': 'Alex', 'last_name': 'Brian'})
    writer.writerow({'Grade': 'A', 'first_name': 'Rachael',
                     'last_name': 'Rodriguez'})
    writer.writerow({'Grade': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'})
    writer.writerow({'Grade': 'B', 'first_name': 'Jane', 'last_name': 'Loive'})
 
print("Writing complete")
"""Primero definimos los fieldnames, los cuales representarán los encabezados de cada columna en el archivo CSV. El método writerrow() escribirá a una fila a la vez. Si quieres escribir todos los datos de una vez, usarás el método writerrows()."""
import csv
 
with open('example5.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name', 'Grade']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 
    writer.writeheader()
    writer.writerows([{'Grade': 'B', 'first_name': 'Alex', 'last_name': 'Brian'},
                      {'Grade': 'A', 'first_name': 'Rachael',
                          'last_name': 'Rodriguez'},
                      {'Grade': 'C', 'first_name': 'Tom', 'last_name': 'smith'},
                      {'Grade': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'},
                      {'Grade': 'A', 'first_name': 'Kennzy', 'last_name': 'Tim'}])
 
print("writing complete")
