from infra.dao.curso_dao import CursoDAO
from business.model.curso_builder import CursoBuilder
from business.service.curso_validation import CursoValidation
from infra.memento.cursos_memento import CursoMemento
import copy
import json

class CursoDAOImpl(CursoDAO):
    def __init__(self, file_path="data/cursos.json"):
        self.file_path = file_path
        self.cursos = self._load_cursos()
        self.validarCurso = CursoValidation()

    def _load_cursos(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data_dict = json.load(file)
                cursos = [
                    CursoBuilder()
                        .com_nome(d['nome'])
                        .com_codigo(d['codigo'])
                        .com_area(d['area'])
                        .com_periodos(d['periodos'])
                        .com_carga_total(d['cargaHorariatotal'])
                        .com_carga_optativa(d['cargaHorariaOptativa'])
                        .com_carga_minima(d['cargaHorariaMinima'])
                        .com_carga_maxima(d['cargaHorariaMaxima'])
                        .com_qtd_favoritos(d['qtdFavoritos'])
                        .construir()
                    for d in data_dict.values()
                ]
                return cursos
        except FileNotFoundError:
            return []


    def _save_cursos(self):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            data_dict = {curso.codigo: curso.to_dict() for curso in self.cursos}
            json.dump(data_dict, file, indent=4)


    def get_curso_by_codigo(self, codigo):
        for curso in self.cursos:
            if curso.codigo == codigo:
                return curso
        return None

    def get_all_cursos(self):
        return self.cursos

    def create_curso(self, curso):
        self.validarCurso.validate_nome(curso.nome)
        self.validarCurso.validate_carga_horaria_total(curso.cargaHorariatotal)
        self.validarCurso.validate_codigo(curso.codigo)
        self.validarCurso.validate_area(curso.area)
        self.validarCurso.validate_periodos(curso.periodos)
        self.validarCurso.validate_carga_horaria_optativa(curso.cargaHorariaOptativa)
        self.validarCurso.validate_carga_horaria_minima(curso.cargaHorariaMinima)
        self.validarCurso.validate_carga_horaria_maxima(curso.cargaHorariaMaxima)
        self.validarCurso.validate_qtd_favoritos(curso.qtdFavoritos)
        self.cursos.append(curso)
        self._save_cursos()

    def update_curso(self, curso, curso_change):
        for i, existing_curso in enumerate(self.cursos):
            if existing_curso.codigo == curso.codigo:
                self.cursos[i].nome = curso_change
                self._save_cursos()
                return
        raise ValueError("Curso não encontrado")

    def delete_curso(self, codigo):
        for i, curso in enumerate(self.cursos):
            if curso.codigo == codigo:
                del self.cursos[i]
                self._save_cursos()
                return
        raise ValueError("Curso não encontrado")
    
    def save_to_memento(self):
        return CursoMemento(copy.deepcopy(self.cursos))
    
    def restore_from_memento(self, memento):
        self.cursos = memento.get_state()
        self._save_cursos() 