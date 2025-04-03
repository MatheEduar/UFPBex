from business.model.curso import Curso
from infra.curso_dao import CursoDAO
from business.controllers.repository.facadeSingleton import FacadeSingleton

class ControllerCursos:
    def __init__(self, dao: CursoDAO):
        self.facade = FacadeSingleton()
        self.dao = dao

    def add(self, nome, codigo, area, periodos, carga_horaria_total, carga_horaria_optativa, carga_horaria_minima, carga_horaria_maxima, qtd_favorito):
        self.facade.add_curso(nome, codigo, area, periodos, carga_horaria_total, carga_horaria_optativa, carga_horaria_minima, carga_horaria_maxima, qtd_favorito)
        print(f"Curso {nome} adicionado com sucesso!")

    def listCurso(self, codigo):
        return self.facade.get_curso(codigo)

    def listAll(self):
        cursos = self.facade.get_all_cursos()
        for curso in cursos:
            print(f"Nome: {curso.nome}, Código: {curso.codigo}, Área: {curso.area}, Períodos: {curso.periodos}, Carga Horária Total: {curso.cargaHorariatotal}, Carga Horária Optativa: {curso.cargaHorariaOptativa}, Carga Horária Mínima: {curso.cargaHorariaMinima}, Carga Horária Máxima: {curso.cargaHorariaMaxima}, Quantidade de Favoritos: {curso.qtdFavoritos}")

    def editCurso(self, codigo, curso_change):
        self.facade.update_curso(codigo, curso_change)
        print(f"Curso {codigo} alterado para {curso_change} com sucesso!")

    def deleteCurso(self, codigo):
        self.facade.delete_curso(codigo)
        print(f"Curso {codigo} deletado com sucesso!")