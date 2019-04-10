#!/usr/bin/env python
# -*- coding: utf-8 -*-
# AGT
# Copyright 2019 Ariel H Garcia Traba <ariel.garcia.traba@gmail.com>
def limpiar():
    import os
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
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
print("##         Unidad 10 - GIT Colaborativo -Pair Programming                 ##");#print("https://www.w3schools.in/python-tutorial/gui-programming/")
print("##            ● Introducción a CVS y comparativa con SVN                  ##");
print("##            ● Creando un repositorio con GIT, clonar, crear branches    ##");
print("##            ● Borrar, guardar (stash), recuperar (pop)                  ##");
print("##            ● Configuración de remote                                   ##");
print("##            ● Configuración de Git avanzada                             ##");
print("##                                                                        ##");
print("############################################################################");
print(input("continuar?"));
print("● ● ● ● ● Ariel sinoptico● ● ● ● ● ");
print("\n ● Programar, manipulacion de datos(objetos) tras su ingreso hasta su salida");
print("\n     Un lenguaje es un conjunto de cadenas de símbolos con los que se pueden crear mensajes. De ese modo los mensajes son transmitidos de un emisor a un receptor. Aún cuando en la naturaleza se pueden identificar ciertos lenguajes, los seres humanos hemos desarrollado lenguajes de diversos tipos y gran complejidad. ");
print("\n     Los lenguajes constan principamente de la gramática, la cual trata sobre la construcción del lenguaje, y la semántica, la cual trata sobre el significado del lenguaje. ");
print("\n        A su vez, la gramática consta de: ");
print("\n             Morfología: cómo se construyen las notaciones (género, tiempos, declinaciones). ");
print("\n            Sintaxis: cómo se deben escribir las notaciones (orden, estructura). ");
print("\n ● Nombre, es la referencia de un dato en un tiempo y espàcio");
print("\n     Nombre : en =/= espacios ,  =  tiempo de ejecucion =/= datos");
print("\n     Nombre : en  =  espacios , =/= tiempo de ejecucion =/= datos");
print("\n ● Objeto, es su espacio con nombre. Individualidad, con caracteristicas");
print("\n     es su materialización de algo incluso un dato");
print("\n     Posee atributos propios o heredados");
print("\n     Genera acciones propias o heredadas");
print("\n ● Funcion-Metodo-Accion-Tarea-Proceso-Verbo");
print("\n     Es el verbo o accion perteneciente a un objeto");
print("\n     Los métodos son bloques de código (o funciones) de una clase que se utilizan para definir el comportamiento de los objetos.");
print("\n ● Atributos definen las características propias del objeto y modifican su estado. Son datos asociados a las clases y a los objetos creados a partir de ellas.");
print("\n     De ello, se deducen los dos tipos de atributos o de variables existentes: variables de clase y variables de instancia (objetos).");
print("\n Tanto para acceder a los atributos como para llamar a los métodos se utiliza el método denominado de notación de punto que se basa en escribir el nombre del objeto o de la clase seguido de un punto y el nombre del atributo o del método con los argumentos que procedan: clase.atributo, objeto.atributo, objeto.método([argumentos]).");
print("\n ● Instanciar, es crear objetos desde una clase.");
print("\n ● Clase, es el razonamiento abstracto de un objeto. Trabajo en distintos capas, en equipo, en grupo, Fron end orientada (al usuario)/ back end (orientada al proceso)");
print("\n ● Las clases en este contexto permiten definir los atributos y el comportamiento, mediante métodos, de los objetos de un programa. Una clase es una especie de plantilla o prototipo que se utiliza para crear instancias individuales del mismo tipo de objeto.");
print("\n ● Ambito, es una region en el espacio donde los nombres (cuyos datos busco) son accesibles directamente.(Recordad que puede haber el mismo nombre como atributo como accion y en distintos ambitos");
print("\n ● Ambito, es observable por estructuras de tabulacion")
print("\n ");
print("\n ● Un espacio con un nombre hereda del Nombre ser la referencia a un dato en un tiempo y espàcio.");
print("\n     Si en el espacio nombrado su dato No cambia durante el tiempo de ejecucion se denomina ● constante (constantes, tuple etc)");
print("\n     Si en el espacio nombrado su dato Si cambia durante el tiempo de ejecucion se denomina ● variable (variable, lista, diccionario, etc");
print("\n     puede haber muchos espacio nombrado igual en distintos ambitos y sus datos podran ser distintos o no");
print("\n     Mutable: su contenido (o dicho valor) puede cambiarse en tiempo de ejecución.");
print("\n     Inmutable: su contenido (o dicho valor) no puede cambiarse en tiempo de ejecución.\n");
print("\n ● Una variable es espacio que tendra un nombre para poder acceder a ella y sus caracteristicas seran dadas por el dato que se incorpore (● tipeado dinamico)");
print("\n ● Una variable de clase es compartida por todas las instancias de una clase. Se definen dentro de la clase (después del encabezado de la clase) pero nunca dentro de un método. Este tipo de variables no se utilizan con tanta frecuencia como las variables de instancia.");
print("\n ● Una variable de instancia se define dentro de un método y pertenece a un objeto determinado de la clase instanciada. ");
print("\n ");
print(input("continuar?"));
limpiar();
print("###########################################################################");
print("##                                                                       ##");
print("##      Unidad 1 -¿Qué es Python?                                        ##");
print("##            ●Instalación y configuración                               ##");
print("##            ●Errores sintácticos y lógicos                             ##");
print("##            ●Programación secuencial                                   ##");
print("##            ●Estructuras condicionales simples, compuestas y anidadas  ##");
print("##            ●Estructuras repetitivas                                   ##");
print("##                                                                       ##");
print("##      Unidad 2 - Variables, Listas                                     ##");
print("##            ●Tipos de variables                                        ##");
print("##            ●Procesamiento de cadenas                                  ##");
print("##            ●Listas                                                    ##");
print("##            ●Diccionarios                                              ##");
print("###########################################################################");
print(input("continuar?"));
print("http://docs.python.org.ar/tutorial/3/classes.html")
print("https://pythonista.io/cursos/py101");
print ("https://pythones.net/instalando-python-3-que-es-un-ide/")
print("\n ")
print("Gracias")
