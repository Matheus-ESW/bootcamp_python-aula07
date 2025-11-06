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

# EX 3

def unicos(lista_valores: List[int]) -> int:
    return len(set(lista_valores))

lista : List[float] = [1, 2, 3, 4, 5, 5, 7, 8, 9, 10]
print(unicos(lista))

# EX 4

def celsius_to_fahrenheit_list(lista_temperaturas: List[float]) -> float:
    return [(9/5) * temp + 32 for temp in lista_temperaturas]

lista : List[float] = [21, 40, 34, 38, 12]
print(celsius_to_fahrenheit_list(lista))

# EX 5

def desvio_padrao(lista_valores: List[float]) -> float:
    media = sum(lista_valores) / len(lista_valores)
    variancia = sum((x - media) ** 2 for x in lista_valores) / len(lista_valores)

    return variancia ** 0.5

lista : List[float] = [1, 2, 3, 4, 5, 5, 7, 8, 9, 10]
print(desvio_padrao(lista))