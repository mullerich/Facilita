def find_text(soup, class_of_element):
    """Retorna o texto de uma determinada classe"""
    texto = soup.find_all(attrs={'class': class_of_element})
    if len(texto) == 0:
        texto = None
    else:
        texto = texto[0].text.strip()
    return texto


def prettify_result(result):
    """Mostra o resultado de uma busca de maneira organizada"""
    print('=' * 150, '\n')
    for info in result:
        if type(result[info]) == list:
            print(f'{info.upper()} ({len(result[info])})')
            for item in result[info]:
                for dado in item:
                    print(f'\t- {dado.upper()}: {item[dado]}')
                print('')
        else:
            print(f'{info.upper()}: \n{result[info]}\n')
