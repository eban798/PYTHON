from tkinter.tix import InputOnly


print("Se necesita obtenerel promedio de un estudiante a partir de sus tres notas parciales N1, N2 Y N3")
N1 = int(input("N1: "))
N2 = int(input("N2: "))
N3 = int(input("N3: "))

P = int( (N1+N2+N3)/3 )
print("\nSalida: ")
print(P)