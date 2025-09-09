def ejercicio2(precio, descuento=10):
   try:
     B = []
     C = 0
     #se empieza con una lista y un contador para poder controlar las veces que se repite
     while C < 3:
        precio = precio - (precio * descuento / 100)
        B.append(precio)
        C += 1
        #calculamos el precio con descuento y lo agregamos a la lista y en contador sube
        print(f"precio con descuento es: {precio}")
        if C < 3:
            precio = int(input("Ingrese el siguiente precio:"))
            #preguntamos otra vez el precio hasta que el contador llegue a 3
   except ValueError:
        print("debe ingresar un numero entero positivo")
        #una excepcion para que el programa no se rompa
