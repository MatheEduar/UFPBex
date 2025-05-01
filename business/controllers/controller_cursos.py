from business.controllers.repository.facade_singleton import FacadeSingleton
from business.report import logger_adapter
from infra.error.data_exception import DataException
from business.service.notificadores import PrintObserver, LoggerObserver
import datetime
from business.service.curso_validation import CursoValidation

class ControllerCursos:
    def __init__(self):
        self.facade = FacadeSingleton()
        self.log = logger_adapter.LoggerAdapter(use_print=True)
        self.observerLog = LoggerObserver()
        self.observerPrint = PrintObserver()
        self.validarCurso = CursoValidation()

    def cursoObservers(self, codigo):
        curso_atual = self.facade.get_curso(codigo)

        curso_atual.adicionar_observador(self.observerLog)
        curso_atual.adicionar_observador(self.observerPrint)

        return curso_atual

    def add(self, nome, codigo, area, periodos, carga_horaria_total, carga_horaria_optativa, carga_horaria_minima, carga_horaria_maxima, qtd_favorito):
        try:

            self.validarCurso.validate_nome(nome)
            self.validarCurso.validate_carga_horaria_total(carga_horaria_total)
            self.validarCurso.validate_codigo(codigo)
            self.validarCurso.validate_area(area)
            self.validarCurso.validate_periodos(periodos)
            self.validarCurso.validate_carga_horaria_optativa(carga_horaria_optativa)
            self.validarCurso.validate_carga_horaria_minima(carga_horaria_minima)
            self.validarCurso.validate_carga_horaria_maxima(carga_horaria_maxima)
            self.validarCurso.validate_qtd_favoritos(qtd_favorito)

            self.facade.add_curso(nome, codigo, area, periodos, carga_horaria_total, carga_horaria_optativa, carga_horaria_minima, carga_horaria_maxima, qtd_favorito)
            curso_atual = self.cursoObservers(codigo)
            curso_atual.notificar_observadores(f"Curso {curso_atual.nome} foi adicionado!")
            self.log.info(f"Curso {nome} adicionado com sucesso!")
        except DataException as e:
            print(f"Erro ao cadastrar curso: {e}")

    def listCurso(self, codigo):
        return self.facade.get_curso(codigo)

    def listAll(self):
        cursos = self.facade.get_all_cursos()
        for curso in cursos:
            self.log.info(f"Nome: {curso.nome}, Código: {curso.codigo}, Área: {curso.area}, Períodos: {curso.periodos}, Carga Horária Total: {curso.cargaHorariatotal}, Carga Horária Optativa: {curso.cargaHorariaOptativa}, Carga Horária Mínima: {curso.cargaHorariaMinima}, Carga Horária Máxima: {curso.cargaHorariaMaxima}, Quantidade de Favoritos: {curso.qtdFavoritos}\n")

    def editCurso(self, codigo, curso_change):
        curso_atual = self.cursoObservers(codigo)
        nome_anterior = curso_atual.nome

        self.facade.update_curso(codigo, curso_change)
        curso_atual.notificar_observadores(f"Nome do curso alterado de '{nome_anterior}' para '{curso_change}'")
        self.log.info(f"Curso {codigo} alterado para {curso_change} com sucesso!")

    def deleteCurso(self, codigo):
        curso_atual = self.cursoObservers(codigo)

        self.facade.delete_curso(codigo)
        curso_atual.notificar_observadores(f"Curso {curso_atual.nome} foi deletado!")
        self.log.info(f"Curso {codigo} deletado com sucesso!")

    def undoAction(self):
        self.facade.undoAction()
        time = datetime.datetime.now()
        self.log.info(f"Ação desfeita: {time}")