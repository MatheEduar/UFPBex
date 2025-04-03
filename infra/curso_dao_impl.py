from infra.curso_dao import CursoDAO
from business.model.curso import Curso

class CursoDAOImpl(CursoDAO):
    def __init__(self, file_path="infra/cursos.txt"):
        self.file_path = file_path
        self.cursos = self._load_cursos()

    def _load_cursos(self):
        try:
            with open(self.file_path, 'r') as file:
                data_list = [line.strip().split(',') for line in file]
                cursos = [Curso(nome, codigo, area, int(periodos), int(carga_horaria_total), int(carga_horaria_optativa), int(carga_horaria_minima), int(carga_horaria_maxima), int(qtd_favorito)) for nome, codigo, area, periodos, carga_horaria_total, carga_horaria_optativa, carga_horaria_minima, carga_horaria_maxima, qtd_favorito in data_list]
                return cursos
        except FileNotFoundError:
            return []

    def _save_cursos(self):
        with open(self.file_path, 'w') as file:
            for curso in self.cursos:
                file.write(f"{curso.nome},{curso.codigo},{curso.area},{curso.periodos},{curso.cargaHorariatotal},{curso.cargaHorariaOptativa},{curso.cargaHorariaMinima},{curso.cargaHorariaMaxima},{curso.qtdFavoritos}\n")

    def get_curso_by_codigo(self, codigo):
        for curso in self.cursos:
            if curso.codigo == codigo:
                return curso
        return None

    def get_all_cursos(self):
        return self.cursos

    def create_curso(self, curso):
        self.cursos.append(curso)
        self._save_cursos()

    def update_curso(self, curso):
        for i, existing_curso in enumerate(self.cursos):
            if existing_curso.codigo == curso.codigo:
                self.cursos[i] = curso
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