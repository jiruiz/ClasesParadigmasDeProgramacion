<<<<<<< HEAD
# lambda es anonima.
# filter para filtrar.
# map para iterar y aplicar una funcion.



# def multiple(numeros):
#     if numeros % 5 == 0:
#         return True
#
numeros = [2,5,10,23,50,33]
#
#resultado = list(filter(multiple, numeros))
# print(resultado)

resultado2 = list(filter(lambda numero: numero%5==0 ,numeros))
print(resultado,resultado2)
=======
numeros = [2, 5, 10, 23, 50, 33]
#
# def multiple(numeros):
#     if numeros % 5 == 0:
#         return True

# resultado = list(filter(multiple, numeros))

resultado2 = list(filter(lambda numero: numero % 5 == 0, numeros))


print(resultado, resultado2)
>>>>>>> 6bee5862327ef143a49f0af6d9c02a125e02c9f5
