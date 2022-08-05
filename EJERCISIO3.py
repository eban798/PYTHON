from asyncore import read, write
from distutils.util import run_2to3
from turtle import write_docstringdict


print ("Respuestas correctas, incorrectas y en blanco")

print ("ingresar numeros de respuesta correctas")
RC = input ("RC: ")

print ("Ingresar numeros de respuestas incorrectas")
RI = input ("RI: ")

print("ingresar numeros de repuestas en blanco")
RB = input("RB: ")

PRC = RC*3
PRI = RI *-1
PRB = RB*0
PF = PRC + PRI + PRB 

print("el puntaje final de cada respuesta es:", PF)