#  EX 1
from typing import List


def media_lista(lista_valores: List[float]) -> float:
    return sum(lista_valores) / len(lista_valores)

lista : List[float] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(media_lista(lista))

