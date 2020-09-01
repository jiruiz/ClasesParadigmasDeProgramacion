#5! = 5*4! = 24    ! es el factorial
#4! = 4*3! = 24   24 es el factorial de 4
#3! = 3*2! = 6
#2! = 2*1! = 2
#1! = 1*0! = 1
#0! = 1
# la recurcion o recursividad es un algoritmo que se llama a si misma n cantidad de veces.
# % * 4 * 3 * 2 * 1

def factorial(numero):
    if numero == 0:
        return 1
    else:
        # print(f"soy el {numero}" )
        # recur = factorial(numero - 1)
        # da = recur * numero
        # return da
        return factorial(numero -1) * numero

#print(factorial(5))

def sacarFibonacci(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return sacarFibonacci(numero - 1) + sacarFibonacci(numero - 2)
print(sacarFibonacci(10))
