class Vagas:
    """Armazena as classes das divs onde contém as informações"""
    def __init__(self):
        self.infos = 'caixa-resultado'      # Caixa que contém as informações gerais do curso
        self.conteudo_box = 'termo-ies'     # Caixa com o título do curso e descrição
        self.faculdade = 'universidade-item'
        self.titulo = 'titulo-box'          # Caixa dentro de termo-ies com o título
        self.descricao = 'texto-box-abi'    # Caixa dentro de termo-ies com a descrição do tipo de curso
        self.texto = 'texto-box'            # Caixa dentro de termo-ies com a descrição da vaga
        self.vaga_box = 'box-reserva'       # Caixas que contém as vagas e suas infos
        self.titulo_vaga = 'titulo-reserva'         # Título da vaga
        self.descricao_vaga = 'reserva-descricao tipo1'     # Descrição da vaga e das quantidades
        self.nota = 'nota-modalidade'       # Data e nota respectiva
