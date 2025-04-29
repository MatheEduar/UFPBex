from business.controllers.repository.facadeSingleton import FacadeSingleton
from business.report import loggerAdapter
from infra.error.dataException import DataException
from business.service.notificadores import PrintObserver, LoggerObserver

class ControllerCursos:
    def __init__(self):
        self.facade = FacadeSingleton()
        self.log = loggerAdapter.LoggerAdapter(use_print=True)

    def add(self, nome, codigo, area, periodos, carga_horaria_total, carga_horaria_optativa, carga_horaria_minima, carga_horaria_maxima, qtd_favorito):
        try:
            self.facade.add_curso(nome, codigo, area, periodos, carga_horaria_total, carga_horaria_optativa, carga_horaria_minima, carga_horaria_maxima, qtd_favorito)
            self.log.info(f"Curso {nome} adicionado com sucesso!")
        except DataException as e:
            print(f"Erro ao cadastrar curso: {e}")

    def listCurso(self, codigo):
        return self.facade.get_curso(codigo)

    def listAll(self):
        cursos = self.facade.get_all_cursos()
        for curso in cursos:
            self.log.info(f"Nome: {curso.nome}, Código: {curso.codigo}, Área: {curso.area}, Períodos: {curso.periodos}, Carga Horária Total: {curso.cargaHorariatotal}, Carga Horária Optativa: {curso.cargaHorariaOptativa}, Carga Horária Mínima: {curso.cargaHorariaMinima}, Carga Horária Máxima: {curso.cargaHorariaMaxima}, Quantidade de Favoritos: {curso.qtdFavoritos}")

    def editCurso(self, codigo, curso_change):
        curso_atual = self.facade.get_curso(codigo)

        curso_atual.adicionar_observador(PrintObserver())
        curso_atual.adicionar_observador(LoggerObserver())

        if curso_atual.nome != curso_change:
            curso_atual.set_nome(curso_change)

        self.facade.update_curso(codigo, curso_change)
        self.log.info(f"Curso {codigo} alterado para {curso_change} com sucesso!")

    def deleteCurso(self, codigo):
        self.facade.delete_curso(codigo)
        self.log.info(f"Curso {codigo} deletado com sucesso!")