"""
Ejercicio 5:
Calcular la potencia de una base elevada a un exponente entero positivo.
"""

def potencia_ciclo(base, exponente):
    resultado =1
    for i in range(exponente):
        resultado *= base
    return resultado


def potencia_recursiva(base, exponente):
    if exponente==0:
        return 1
    return base * potencia_recursiva(base, exponente-1)

base = 2
exponente = 5

print(potencia_ciclo(base, exponente))
print(potencia_recursiva(base, exponente))
