def ejercicio4():
   try:
     A=int(input("ingrese un numero entero:"))
     B=int(input("ingrese un numero entero:"))
     Resultado=A/B
     #usamos el try y hacemos un codigo basico para calcular una division
     print(f"resultado: {Resultado}")
   except ValueError:
     print("debe ingresar un numero entero")
   except ZeroDivisionError:
     print("no puedes ingresar 0")
     #despues de hacer el codigo basico usamos las excepciones para controlar los errores
