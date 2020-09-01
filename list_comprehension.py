<<<<<<< HEAD

#ejemplo 1
# lista = []
#
# for numero in range(0,11):
#     lista.append(numero**2)
#
# print(lista)
#
# lista_c = [numero**2 for numero in range(0,11)]
# print(lista_c)

#ejemplo 2
lista = []
for numero in range(0,11):
    if numero%2 == 0:
        lista.append(numero**2)

print(lista)

lista_c = [numero**2 for numero in range(0,11) if numero%2==0]
=======
# ejemplo 1
# lista = []
# for numero in range(0,11):
#     lista.append(numero ** 2)
# print(lista)
#
# lista_c = [numero **2 for numero in range(0,11)]
# print(lista_c)


# ejemplo 2
lista = []
for numero in range(0,11):
    if numero % 2 == 0:
        lista.append(numero ** 2)
print(lista)


lista_c = [numero **2 for numero in range(0,11) if numero % 2 == 0]
>>>>>>> 6bee5862327ef143a49f0af6d9c02a125e02c9f5
print(lista_c)
