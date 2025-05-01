from abc import ABC, abstractmethod

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

    @abstractmethod
    def save_to_memento(self):
        pass

    @abstractmethod
    def restore_from_memento(self,memento):
        pass

    