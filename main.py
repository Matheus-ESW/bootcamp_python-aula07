#  EX 1
from typing import List


def media_lista(lista_valores: List[float]) -> float:
    return sum(lista_valores) / len(lista_valores)

lista : List[float] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(media_lista(lista))

# EX 2

def filtrar_valores(lista_valores: List[float], limite: float) -> list:
    valores_filtrados = []
    for valores in lista_valores:
        if valores > limite:
            valores_filtrados.append(valores)
    
    return valores_filtrados

lista : List[float] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
limite = 6
print(filtrar_valores(lista, limite))