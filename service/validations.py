from error.exceptionPassword import ExceptionPassword
from error.exceptionUser import ExceptionUser
import re

class Validation:
    def __init__(self):
        pass

    def validateUserName(self, username):

        if not username:
            raise ExceptionUser("Entrada inválida. O Nick não pode estar vazio!")
        elif len(username) > 12:
            raise ExceptionUser("Entrada inválida. O Nick não pode ultrapassar 12 caracteres!")
        elif any(char.isdigit() for char in username):
            raise ExceptionUser("Entrada inválida. O Nick não pode conter números!")

    def validatePassword(self, senha):
        if not (8 <= len(senha) <= 128):
            raise ExceptionPassword("Entrada inválida. A senha deve ter entre 8 e 128 caracteres!")

        # Contadores para tipos de caracteres
        tem_maiuscula = bool(re.search(r'[A-Z]', senha))
        tem_minuscula = bool(re.search(r'[a-z]', senha))
        tem_numero = bool(re.search(r'\d', senha))
        tem_especial = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{}|\'"]', senha))

        # Conta quantos tipos diferentes a senha contém
        tipos_presentes = sum([tem_maiuscula, tem_minuscula, tem_numero, tem_especial])

        if tipos_presentes < 3:
            raise ExceptionPassword("Entrada inválida. A senha deve conter pelo menos três dos seguintes tipos de caracteres: maiúsculas, minúsculas, números e caracteres especiais!")
