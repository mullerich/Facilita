"""
Esse programa tem o intuito de ler as tabelas de relatório disponibilizadas pelo INEP
https://sisu.mec.gov.br/#/relatorio#onepage e coletar os dados

Os dados importantes a serem extraídos são:

NU_ANO: Ano do processo seletivo
NU_EDICAO:	Número da edição do processo seletivo no ano de referência
CO_IES:	Código da instituição de ensino superior confome informações do cadastro e-MEC
NO_IES:	Nome da instituição de ensino superior confome informações do cadastro e-MEC
SG_IES:	Sigla da instituição de ensino superior confome informações do cadastro e-MEC
DS_ORGANIZACAO_ACADEMICA:	Descrição da organização acadêmica da instituição de ensino superior confome informações do cadastro e-MEC
DS_CATEGORIA_ADM:	Descrição da categoria administrativa da instituição de ensino superior confome informações do cadastro e-MEC
NO_CAMPUS:	Nome do campus da instituição de ensino superior confome informações do cadastro e-MEC
NO_MUNICIPIO_CAMPUS:	Nome do município do campus da instituição de ensino superior confome informações do cadastro e-MEC
SG_UF_CAMPUS:	Sigla da unidade da federação (UF) na qual está localizada o campus da instituição de ensino superior confome informações do cadastro e-MEC
DS_REGIAO_CAMPUS:	Descrição da região na qual está localizada o campus da instituição de ensino superior confome informações do cadastro e-MEC
CO_IES_CURSO:	Código do curso da instituição de ensino superior confome informações do cadastro e-MEC
NO_CURSO:	Nome do curso da instituição de ensino superior confome informações do cadastro e-MEC
DS_GRAU:	Grau do curso da instituição de ensino superior confome informações do cadastro e-MEC
DS_TURNO:	Turno do curso da instituição de ensino superior confome informações do cadastro e-MEC
TP_MODALIDADE:	Tipo da modalidade da oferta do curso no processo seletivo
DS_MOD_CONCORRENCIA:	Descrição do tipo da modalidade de concorrência ofertada para o curso no processo seletivo
NU_PERCENTUAL_BONUS:	Percentual de bônus definido para as ações afirmativas próprias das IES
QT_VAGAS_CONCORRENCIA:	Quantidade de vagas ofertadas naquela modalidade
NU_NOTACORTE:	Nota de corte da modalidade/curso conforme o resultado da chamada regular. A nota de corte é sempre igual a nota do último candidato classificado na última vaga ofertada para a modalidade/curso escolhida. Na modalidade de bônus a nota de corte é a mesma da modalidade ampla concorrência do mesmo curso porque as pessoas que se inscreveram na modalidade bônus concorrem pelas vagas ofertadas para ampla concorrência do mesmo curso/grau/turno/campus/IES. Alguns cursos podem não apresentar nota de corte pois não tiveram número de inscritos pelo menos igual ao número de vagas ou porque tiveram poucos inscritos e alguns desses inscritos tiveram seleção na 1ª opção de curso e, portanto, não têm sua nota considerada para sua 2ª opção de inscrição
QT_INSCRICAO:	Quantidade de inscrições para a modalidade
"""

from openpyxl import load_workbook

def leitor(nome_arquivo, ano, edicao):
    excel_data = load_workbook(nome_arquivo, read_only=True)
    datasheet = excel_data[f'inscricao_{ano}_{edicao}']     # Folha inscricao_2019_2
    colunas = datasheet.max_column
    linhas = datasheet.max_row

    dados = {}
    for c in range(1, 5+1):
        dados[f"{datasheet.cell(1, c).value}"] = []

    print(dados)
    for col in range(1, 5+1):
        titulo_coluna = datasheet.cell(1, col).value
        for row in range(2, 5+1):
            print(titulo_coluna, datasheet.cell(row=row, column=col).value)
            dados[titulo_coluna].append(datasheet.cell(row=row, column=col).value)

    return dados


print(leitor('2019_2.xlsx', 2019, 2))
