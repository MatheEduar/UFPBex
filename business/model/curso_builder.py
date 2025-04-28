from business.model.curso import Curso

class CursoBuilder:
    def __init__(self):
        self.curso = Curso()

    def com_nome(self, nome):
        self.curso.nome = nome
        return self

    def com_codigo(self, codigo):
        self.curso.codigo = codigo
        return self

    def com_area(self, area):
        self.curso.area = area
        return self

    def com_periodos(self, periodos):
        self.curso.periodos = periodos
        return self

    def com_carga_total(self, total):
        self.curso.cargaHorariatotal = total
        return self

    def com_carga_optativa(self, optativa):
        self.curso.cargaHorariaOptativa = optativa
        return self

    def com_carga_minima(self, minima):
        self.curso.cargaHorariaMinima = minima
        return self

    def com_carga_maxima(self, maxima):
        self.curso.cargaHorariaMaxima = maxima
        return self

    def com_qtd_favoritos(self, qtd):
        self.curso.qtdFavoritos = qtd
        return self

    def construir(self):
        return self.curso