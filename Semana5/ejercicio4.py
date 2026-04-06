"""
Ejercicio 4:
Dado un número entero positivo N, contar cuántos números pares existen entre 1 y N.
"""

def contar_pares_ciclo(n):
    contador=0
    for i in range(1, n+1):
        if i % 2 ==0:
            contador +=i
    return contador




def contar_pares_recursivo(n):
    if n ==1:
        return 0
    if n %2 ==0:
        return 1 + contar_pares_recursivo(n-1)
    else:
        return contar_pares_recursivo(n-1)
n=10
print(contar_pares_ciclo(n))
print(contar_pares_recursivo(n))