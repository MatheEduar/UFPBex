from .repositoryFactory import RepositoryFactory
from business.model.user import User
from business.model.curso_builder import CursoBuilder

class FacadeSingleton:
    _instance = None
    user_repository = None
    curso_repository = None

    def __new__(self):
        if FacadeSingleton._instance is None:
            FacadeSingleton._instance = super(FacadeSingleton, self).__new__(self)
            FacadeSingleton.user_repository = RepositoryFactory.create_user_repository()
            FacadeSingleton.curso_repository = RepositoryFactory.create_curso_repository()    
        return FacadeSingleton._instance

    def add_user(self, username, password):
        user = User(username, password)
        FacadeSingleton.user_repository.create_user(user)

    def get_user(self, username):
        return FacadeSingleton.user_repository.get_user_by_username(username)

    def get_all_users(self):
        return FacadeSingleton.user_repository.get_all_users()

    def update_user(self, username, userChange):
        user = FacadeSingleton.user_repository.get_user_by_username(username)
        if user:
            user.username = userChange
            FacadeSingleton.user_repository.update_user(user)

    def delete_user(self, username):
        FacadeSingleton.user_repository.delete_user(username)

    def add_curso(self, nome, codigo, area, periodos, carga_horaria_total, carga_horaria_optativa, carga_horaria_minima, carga_horaria_maxima, qtd_favorito):
        curso = (CursoBuilder()
             .com_nome(nome)
             .com_codigo(codigo)
             .com_area(area)
             .com_periodos(periodos)
             .com_carga_total(carga_horaria_total)
             .com_carga_optativa(carga_horaria_optativa)
             .com_carga_minima(carga_horaria_minima)
             .com_carga_maxima(carga_horaria_maxima)
             .com_qtd_favoritos(qtd_favorito)
             .construir())
        
        FacadeSingleton.curso_repository.create_curso(curso)

    def get_curso(self, codigo):
        return FacadeSingleton.curso_repository.get_curso_by_codigo(codigo)

    def get_all_cursos(self):
        return FacadeSingleton.curso_repository.get_all_cursos()

    def update_curso(self, codigo, curso_change):
        curso = FacadeSingleton.curso_repository.get_curso_by_codigo(codigo)
        if curso:
            curso.nome = curso_change
            FacadeSingleton.curso_repository.update_curso(curso)

    def delete_curso(self, codigo):
        FacadeSingleton.curso_repository.delete_curso(codigo)