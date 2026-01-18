"""
Ejemplo de 3 buenos hábitos en Python:
1. Uso de if __name__ == "__main__"
2. Type annotations
3. List comprehensions
"""
from typing import List

def saludar( name: str) -> None:
    print(f"Hola {name}")

def numeros_al_cuadrado(numeros: List[int]) -> List[int]:
    return print([n * n for n in numeros])


if __name__ == '__main__':
    saludar("Roberto")
    numeros_al_cuadrado([1,2,3])

