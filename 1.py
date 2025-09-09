
def ejercicio1():
 B=[]
 try:
  A = int(input("ingrese un numero positivo:"))
   #iniciamos con una lista y un input para preguntar el numero entero positivo
  if A >= 0:
   for i in range(2, A + 1):
    for j in range(2, i):
     if i % j == 0:
      break
     #utilizamos un for para recorrer los numeros y otro for para verificar si son primos
    else:
     B.append(i)
   print(f"numeros totales {B}")
   print(f"Cantidad de primos: {len(B)}")
  elif A < 0:
   print("el numero no es positivo")
   #agregamos los numeros a la lista y hacemos dos prinst para mostrar los resultados
 except ValueError:
   print("debe ingresar un numero entero positivo")
  
