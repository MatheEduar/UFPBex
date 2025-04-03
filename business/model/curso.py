class Curso:
    def __init__(self, nome, codigo, area, periodos, carga_horaria_total, carga_horaria_optativa, carga_horaria_minima, carga_horaria_maxima, qtd_favorito):
        self.nome = nome
        #self.descricao = descricao
        self.cargaHorariatotal = carga_horaria_total
        self.codigo = codigo
        self.area = area
        self.periodos = periodos
        #self.disciplinas = disciplinas
        self.cargaHorariaOptativa = carga_horaria_optativa
        self.cargaHorariaMinima = carga_horaria_minima
        self.cargaHorariaMaxima = carga_horaria_maxima
        self.qtdFavoritos = qtd_favorito