from abc import ABC, abstractmethod
from business.model.curso import Curso

class CursoDAO(ABC):
    @abstractmethod
    def get_curso_by_codigo(self, codigo):
        pass

    @abstractmethod
    def get_all_cursos(self):
        pass

    @abstractmethod
    def create_curso(self, curso):
        pass

    @abstractmethod
    def update_curso(self, curso):
        pass

    @abstractmethod
    def delete_curso(self, codigo):
        pass