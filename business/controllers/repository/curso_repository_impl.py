from infra.dao.curso_dao_impl import CursoDAOImpl
from business.service.curso_validation import CursoValidation
from business.controllers.repository.curso_repository import CursoRepository
from infra.memento.cursos_caretaker import CursoCaretaker  

class CursoRepositoryImpl(CursoRepository):
    def __init__(self):  
        self.dao = CursoDAOImpl()
        self.caretaker = CursoCaretaker(self.dao)
        self.validtaion = CursoValidation()

    def get_curso_by_codigo(self, codigo):
        return self.dao.get_curso_by_codigo(codigo)

    def get_all_cursos(self):
        return self.dao.get_all_cursos()

    def create_curso(self, curso):
        self.caretaker.backup()
        self.dao.create_curso(curso)

    def update_curso(self, curso, curso_change):
        self.caretaker.backup()
        self.dao.update_curso(curso, curso_change)

    def delete_curso(self, codigo):
        self.caretaker.backup()
        self.dao.delete_curso(codigo)
    
    def undoAction(self):
        self.caretaker.undo()