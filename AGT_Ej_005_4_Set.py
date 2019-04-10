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
print("##         Unidad 10 - GIT Colaborativo -Pair Programming                 ##");#print("https://www.w3schools.in/python-tutorial/gui-programming/")
print("##            * Introducción a CVS y comparativa con SVN                  ##");
print("##            * Creando un repositorio con GIT, clonar, crear branches    ##");
print("##            * Borrar, guardar (stash), recuperar (pop)                  ##");
print("##            * Configuración de remote                                   ##");
print("##            * Configuración de Git avanzada                             ##");
print("##                                                                        ##");
print("############################################################################");
print("##                                                                        ##");
print("##      Unidad 1 -¿Qué es Python?                                         ##");
print("##            * Instalación y configuración                               ##");
print("##            * Errores sintácticos y lógicos                             ##");
print("##            * Programación secuencial                                   ##");
print("##            * Estructuras condicionales simples, compuestas y anidadas  ##");
print("##            * Estructuras repetitivas                                   ##");
print("##                                                                        ##");
print("############################################################################");
print("##                                                                        ##");
print("##                      Python Set /Array Methods                         ##");
print("##                     ---------------------------                        ##");
print("##                                                                        ##");
print("##     Method    Description                                              ##");
print("##                                                                        ##");
print("##     add()     Adds an element to the set                               ##");
print("##     clear()   Removes all the elements from the set                    ##");
print("##     copy()    Returns a copy of the set                                ##");
print("##     difference()	Returns a set containing the difference between two  ##");
print("##               or more sets                                             ##");
print("##     difference_update()	Removes the items in this set that are also  ##");
print("##                included in another, specified set                      ##");
print("##     discard()	Remove the specified item                                ##");
print("##     intersection()	Returns a set, that is the intersection of two   ##");
print("##                other sets                                              ##");
print("##     intersection_update()	Removes the items in this set that are not   ##");
print("##               present in other, specified set(s)                       ##");
print("##     isdisjoint()	Returns whether two sets have a intersection or      ##");
print("##                not                                                     ##");
print("##     issubset()	Returns whether another set contains this set or     ##");
print("##                not                                                     ##");
print("##     issuperset()	Returns whether this set contains another set or     ##");
print("##                not                                                     ##");
print("##     pop()	Removes an element from the set                              ##");
print("##     remove()	Removes the specified element                            ##");
print("##     symmetric_difference()	Returns a set with the symmetric         ##");
print("##                differences of two sets                                 ##");
print("##     symmetric_difference_update()	inserts the symmetric differences    ##");
print("##                from this set and another                               ##");
print("##     union()	Return a set containing the union of sets                ##");
print("##     update()	Update the set with the union of this set and others     ##");
print("##                                                                        ##");
print("############################################################################");
print("##                                                                        ##");
print("##                                  SET                                   ##");
print("##                                                                        ##");
print("##  Un conjunto es una lista de elementos donde ninguno de ellos está     ##");
print("##  repetido. A partir de una lista, en la que pueden haber elementos     ##");
print("##  repetidos, con set es posible crear otra lista con todos los          ##");
print("##  elementos pero sin repetir ninguno. Además, si tenemos varias         ##");
print("##  listas podemos realizar operaciones de conjuntos de unión,            ##");
print("##  diferencia, intersección y diferencia simétrica                       ##");
print("##                                                                        ##");
print("############################################################################");
print("https://www.w3schools.com/python/python_sets.asp");
print (input("Fin    continuar?"));
Nombre_set_1 = {"linea 1","linea 2","linea 3","linea 4","linea 5","linea 6","linea 7","linea 8","linea 9","linea 1"}
print("#########################################################");
# Ej 007_1
print("Inicio 007_SET_1")
print("Access Items\nYou cannot access items in a set by referring to an indedato_set, since sets are unordered the items has no indedato_set.");
print("But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.");
print("Loop through the set, and print the values:")
for dato_set in Nombre_set_1:  print(dato_set)
print (input("Fin Fin ej007_SET_1 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 007_2
print("Inicio 007_SET_2")
print("Check");
print("----------");
print("Check if 'linea 5' is present in the set:")
print("linea 2" in Nombre_set_1)
if ("linea 2" in Nombre_set_1):  print("Si, esta en lista!")
print (input("Fin Fin ej007_SET_2 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 007_3
print("Inicio 007_SET_3")
print("Change Items");
print("Once a set is created, you cannot change its items, but you can add new items.");
print("Add Items");
print("---------");
print("Add an item to a set, using the add() method:");
print(Nombre_set_1)
Nombre_set_1.add("linea 0")
print(Nombre_set_1)
print (input("Fin Fin ej007_SET_3 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 007_4
print("Inicio 007_SET_4")
print("Add multiple items to a set, using the update() method:");
print(Nombre_set_1)
Nombre_set_1.update(["linea 11", "linea 12", "linea 13"])
print(Nombre_set_1)
print (input("Fin Fin ej000_SET_4 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 007_5
print("Inicio 007_SET_5")
print("Get the Length of a Set");
print("-----------------------");
print("To determine how many items a set has, use the len() method.");
print("Get the number of items in a set:");
print(len(Nombre_set_1))
print (input("Fin Fin ej000_SET_5 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 007_6
print("Inicio 007_SET_6")
print("Remove Item");
print("-----------");
print("To remove an item in a set, use the remove(), or the discard() method.");
print("Remove 'linea 4' by using the remove() method:");
print(Nombre_set_1)
Nombre_set_1.remove("linea 4")
print(Nombre_set_1)
print("Note: If the item to remove does not erase all list, remove() will raise an error.");
print (input("Fin Fin ej000_SET_6 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 007_7
print("Inicio 007_SET_7")
print("Remove 'linea 3' by using the discard() method:");
print(Nombre_set_1)
Nombre_set_1.discard("linea 3")
print(Nombre_set_1)
print("Note: If the item to remove does erase all list, discard() will NOT raise an error.");
print (input("Fin Fin ej000_SET_7 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 007_8
print("Inicio 007_SET_8")
print("You can also use the pop(), method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.");
print("The return value of the pop() method is the removed item.");
print("Remove the last item by using the pop() method:");
dato_set = Nombre_set_1.pop()
print(dato_set)
print(Nombre_set_1)
print("Note: Sets are unordered, so when using the pop() method, you will not know which item that gets removed.");
print (input("Fin Fin ej000_SET_8 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 007_9
print("Inicio 007_SET_9")
print("Clear Item");
print("----------");
print("The clear() method empties the set:");
Nombre_set_1.clear()
print(Nombre_set_1)
print("The del keyword will delete the set completely:");
print (input("Fin Fin ej000_SET_9 \n		continuar?"));
limpiar();
print("#########################################################");
# Ej 007_10
print("Inicio 007_SET_10")
print("Del Item");
print("--------");
print("The 'del' erase the set:");
del Nombre_set_1
print(Nombre_set_1)
print("The del keyword will delete the set completely:");
print (input("Fin Fin ej000_SET_10 \n		continuar?"));
