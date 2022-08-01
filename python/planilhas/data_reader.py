"""
Esse programa tem o intuito de ler as tabelas de relatório disponibilizadas pelo INEP
https://sisu.mec.gov.br/#/relatorio#onepage, coletar os dados e transformar em lista
"""
from pandas import read_excel, ExcelFile
import os


def leitor_xlsx(nome_arquivo, colunas=[]):
    """Lê determinadas colunas de um determinado arquivo excel"""
    nome_folha = ExcelFile(nome_arquivo).sheet_names[1]
    colunas_lidas = list(read_excel(nome_arquivo, nome_folha, nrows=1).columns)
    colunas_usadas = [n for n, e in enumerate(colunas_lidas) if e in colunas] if colunas != [] else [x for x in range(len(colunas_lidas))]
    data = read_excel(nome_arquivo, nome_folha, usecols=colunas_usadas, skiprows=1).values
    return data


def listar_xlsx(path):
    """Lista todos os arquivos xlsx em um determinado diretório."""
    planilhas = [arq for arq in os.listdir(path) if arq.endswith('.xlsx')]
    return planilhas


#leitor_xlsx('./planilhas/vagas/Portal Sisu_Sisu 2019-2_Vagas ofertadas.xlsx')