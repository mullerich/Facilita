"""
Esse programa tem o intuito de ler as tabelas de relatório disponibilizadas pelo INEP
https://sisu.mec.gov.br/#/relatorio#onepage, coletar os dados e transformar em lista
"""

from openpyxl import load_workbook
from pandas import read_excel

def open_excel(nome_arquivo, nome_folha, colunas=[]):
    return read_excel(nome_arquivo, nome_folha, skiprows=1, usecols=colunas)


def leitor(datasheet):
    data = datasheet.values
    return list(data)


def which_column(nome_arquivo, nome_folha, colunas):
    """
    Determina o valor numérico de colunas de uma folha de planilha
    """
    excel_data = load_workbook(nome_arquivo, read_only=True)
    datasheet = excel_data[nome_folha]  
    num_colunas = datasheet.max_column
    colunas_usadas = []
    
    if colunas == []:
        colunas_usadas = None

    else:
        for c in range(1, num_colunas+1):
            if datasheet.cell(1, c).value in colunas:
                colunas_usadas.append(c-1)
    
    return colunas_usadas

