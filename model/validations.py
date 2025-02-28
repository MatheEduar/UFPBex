from exceptions import InvalidPasswordException, InvalidUsernameException
import re

def nickValidation(nick):

    if not nick:
        raise InvalidUsernameException("Entrada inválida. O Nick não pode estar vazio!")
    elif len(nick) > 12:
        raise InvalidUsernameException("Entrada inválida. O Nick não pode ultrapassar 12 caracteres!")
    elif any(char.isdigit() for char in nick):
        raise InvalidUsernameException("Entrada inválida. O Nick não pode conter números!")

    return True 

def passwordValidation(senha, nome, email):
    if not (8 <= len(senha) <= 128):
        raise InvalidPasswordException("Entrada inválida. A senha deve ter entre 8 e 128 caracteres!")

    # Contadores para tipos de caracteres
    tem_maiuscula = bool(re.search(r'[A-Z]', senha))
    tem_minuscula = bool(re.search(r'[a-z]', senha))
    tem_numero = bool(re.search(r'\d', senha))
    tem_especial = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{}|\'"]', senha))

    # Conta quantos tipos diferentes a senha contém
    tipos_presentes = sum([tem_maiuscula, tem_minuscula, tem_numero, tem_especial])
    
    if tipos_presentes < 3:
        raise InvalidPasswordException("Entrada inválida. A senha deve conter pelo menos três dos seguintes tipos de caracteres: maiúsculas, minúsculas, números e caracteres especiais!")

    if senha.lower() in [nome.lower(), email.lower()]:
        raise InvalidPasswordException("Entrada inválida. A senha não pode ser idêntica ao nome ou ao e-mail!")

    return True 