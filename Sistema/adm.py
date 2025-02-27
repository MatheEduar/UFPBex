from usuario import Usuario

class Adm(Usuario):
    def __init__(self,nome,username,email,senha):
        super().__init__(nome, username, email, senha)

    def ListarUsuarios(lista):
        for users in lista:
            print(f"Nome: {users.nome}, Username: {users.username}, Email: {users.email}")

    def BloquearUsuario(usuario,lista):
        lista.append(usuario)
