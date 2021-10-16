from webdriver import WebDriver


def prettify_result(result):
    print('='*150, '\n')
    for info in result:
        if type(result[info]) == list:
            print(f'{info.upper()} ({len(result[info])})')
            for item in result[info]:
                for dado in item:
                    print(f'\t- {dado.upper()}: {item[dado]}')
                print('')
        else:
            print(f'{info.upper()}: \n{result[info]}\n')


links = ['https://sisu.mec.gov.br/#/vagas/detalhe?coOferta=197399#target', 'https://sisu.mec.gov.br/#/vagas/detalhe?coOferta=198842#target', 'https://sisu.mec.gov.br/#/vagas/detalhe?coOferta=197386#target']
vaga = WebDriver()
for link in links:
    vaga.url = link
    resultado = vaga.coletar_vaga()
    prettify_result(resultado)

vaga.close()

'''
drive = WebDriver()
cursos = drive.coletar_cursos()
drive.close()
prettify_result(cursos)'''
