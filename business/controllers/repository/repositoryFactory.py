from .userRepositoryIMPL import UserRepositoryImpl
from .cursoRepositoryIMPL import CursoRepositoryImpl
class RepositoryFactory:
    @staticmethod
    def create_user_repository():
        return UserRepositoryImpl()
    
    @staticmethod
    def create_curso_repository():
        return CursoRepositoryImpl()