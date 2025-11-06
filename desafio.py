# DESAFIO

from typing import List
import csv

def ler_csv(arquivo_csv: str) -> List[dict]:

    lista_dicionario = []

    with open(arquivo_csv, 'r', encoding="utf-8") as arquivo:
        dicionario = csv.DictReader(arquivo)

        for linha in dicionario:
            lista_dicionario.append(dict(linha))
    
    return lista_dicionario

def processar_dados(lista_dados: list[dict]) -> dict:
    resultado = {}

    for item in lista_dados:
        categoria = item.get("Categoria")
        produto = item.get("Produto")
        quantidade = int(item.get("Quantidade", 0))
        venda = float(item.get("Venda", 0))

        # Se a categoria ainda não existe no dicionário, cria uma lista
        if categoria not in resultado:
            resultado[categoria] = []

        # Adiciona os dados formatados dentro da categoria
        resultado[categoria].append({
            "Produto": produto,
            "Quantidade": quantidade,
            "Venda": venda
        })

    return resultado

def calcular_vendas_categoria(dados_processados: dict) -> dict:
    total_por_categoria = {}

    for categoria, lista_produtos in dados_processados.items():
        total = 0

        for item in lista_produtos:
            quantidade = item.get("Quantidade", 0)
            venda = item.get("Venda", 0)
            total += quantidade * venda
        
        total_por_categoria[categoria] = total
    
    return total_por_categoria


def main():
    raw_data = ler_csv('vendas.csv')
    processed_data = processar_dados(raw_data)
    vendas_por_categoria = calcular_vendas_categoria(processed_data)
    print(vendas_por_categoria)

if __name__ == '__main__':
    main()