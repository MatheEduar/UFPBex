from infra.curso_dao_impl import CursoDAOImpl
from business.service.cursoValidation import CursoValidation
from infra.cursoRepository import CursoRepository  

class CursoRepositoryImpl(CursoRepository):
    def __init__(self):  
        self.dao = CursoDAOImpl()
        self.validtaion = CursoValidation()

    def get_curso_by_codigo(self, codigo):
        return self.dao.get_curso_by_codigo(codigo)

    def get_all_cursos(self):
        return self.dao.get_all_cursos()

    def create_curso(self, curso):
        
        self.dao.create_curso(curso)

    def update_curso(self, curso):
        self.dao.update_curso(curso)

    def delete_curso(self, codigo):
        self.dao.delete_curso(codigo)