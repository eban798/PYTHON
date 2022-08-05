import math


print("Ejercicio5: NÚMERO DE MICRO DISCOS 3.5 NECESARIOS")

print("Ingrese GB: ")
GB = float( input())

MG = GB*1024
MD = MG/1.44

print("\nSALIDA: ")

print(MD)

print("Numero Discos necesarios: ", math .ceil(MD))