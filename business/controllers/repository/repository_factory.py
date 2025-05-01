from .user_repository_impl import UserRepositoryImpl
from .curso_repository_impl import CursoRepositoryImpl
class RepositoryFactory:
    @staticmethod
    def create_user_repository():
        return UserRepositoryImpl()
    
    @staticmethod
    def create_curso_repository():
        return CursoRepositoryImpl()