from usuario import Usuario

class Adm(Usuario):
    def __init__(self,nome,username,senha,email):
        super().__init__(nome, username, senha, email)

    def ListarUsuarios(lista):
        for users in lista:
            print(f"Nome: {users.nome}, Username: {users.username}, Email: {users.email}")

    def BloquearUsuario(usuario,lista):
        lista.append(usuario)
