def ejercicio3(*args, **kwargs):
  #comenzamos con un condicional y una variable para contar las vocales
  if kwargs.get('contar_vocales'):
    total_vocales = 0
    for texto in args:
      total_vocales += sum(1 for c in texto if c in 'aeiou')
    print(f"Cantidad total de vocales: {total_vocales}")
    #usamos un for para recorrer los textos y una sum para contar las vocales
  else:
    total_palabras = 0
    for texto in args:
      total_palabras += len(texto.split())
    print(f"Cantidad total de palabras: {total_palabras}")
    #terminamos con otro for para contar las palabras

ejercicio3("hola mundo", "python es genial", contar_vocales=True)
