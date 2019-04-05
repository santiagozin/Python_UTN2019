#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  yield.py
#  
#  Copyright 2019 Ariel H Garcia Traba <AGT@AGT>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

#  
#  

# Ej 008_3

print("Inicio ej008_3 - yield")
def numeros_pares(maximo):
	contador = 1
	while contador<maximo:
		yield contador*2
		contador=contador+1
resultados = numeros_pares(10)
for i in resultados:
	print (resultados)
print("Fin ej008_2"); print("")
# Declara generador
input()
def gen_basico():
    yield "uno"   
    yield "dos"
    yield "tres"
   
for valor in gen_basico():
    print(valor)  # uno, dos, tres

# Crea objeto generador y muestra tipo de objeto

generador = gen_basico()
print(generador)  # generator object gen_basico at 0x7f75ffad55e8
print(type(generador))  # class 'generator'

# Convierte a lista el objeto generador y muestra elementos

lista = list(generador)
print(lista)  # ['uno', 'dos', 'tres']
print(type(lista))  # class 'list'
