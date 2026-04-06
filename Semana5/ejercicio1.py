"""
Ejercicio 1: Dado un número entero positivo N, retornar una lista con los números desde 1 hasta N.

Debe implementar dos funciones:
1. Una usando iteración (for o while)
2. Una usando recursividad
"""

def contar_ciclo(n):
    lista = []
    for i in range (1, n+1):
        lista.append(i)
    return lista


def contar_recursivo(n):
    if n ==1:
        return[1]
    return contar_recursivo (n-1)+[n]

print(contar_ciclo(5))
print(contar_recursivo(5))
