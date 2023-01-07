print ("Ingrese Cantidad de datos")
n=int(input())
acum=0                              
for i in range(0,n):
  print ("Ingresa los números para el promedio")
  dato=int(input())
  acum= acum+dato
prom=acum/n
print("El promedio es: ", prom)