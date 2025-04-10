from business.model.curso import Curso
from infra.curso_dao import CursoDAO
from business.controllers.repository.facadeSingleton import FacadeSingleton
from business.report import loggerAdapter

class ControllerCursos:
    def __init__(self, dao: CursoDAO):
        self.facade = FacadeSingleton()
        self.dao = dao
        self.log = loggerAdapter.LoggerAdapter(use_print=True)

    def add(self, nome, codigo, area, periodos, carga_horaria_total, carga_horaria_optativa, carga_horaria_minima, carga_horaria_maxima, qtd_favorito):
        self.facade.add_curso(nome, codigo, area, periodos, carga_horaria_total, carga_horaria_optativa, carga_horaria_minima, carga_horaria_maxima, qtd_favorito)
        self.log.info(f"Curso {nome} adicionado com sucesso!")

    def listCurso(self, codigo):
        return self.facade.get_curso(codigo)

    def listAll(self):
        cursos = self.facade.get_all_cursos()
        for curso in cursos:
            self.log.info(f"Nome: {curso.nome}, Código: {curso.codigo}, Área: {curso.area}, Períodos: {curso.periodos}, Carga Horária Total: {curso.cargaHorariatotal}, Carga Horária Optativa: {curso.cargaHorariaOptativa}, Carga Horária Mínima: {curso.cargaHorariaMinima}, Carga Horária Máxima: {curso.cargaHorariaMaxima}, Quantidade de Favoritos: {curso.qtdFavoritos}")

    def editCurso(self, codigo, curso_change):
        self.facade.update_curso(codigo, curso_change)
        self.log.info(f"Curso {codigo} alterado para {curso_change} com sucesso!")

    def deleteCurso(self, codigo):
        self.facade.delete_curso(codigo)
        self.log.info(f"Curso {codigo} deletado com sucesso!")