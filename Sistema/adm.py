import usuario
class Adm(usuario.Usuario):
    def __init__(self,nome,username,senha,email):
            self.nome = nome 
            self.username = username
            self.senha = senha
            self.email = email
    def ListarUsuarios(lista):
        for users in lista:
            print(users)
    def BloquearUsuario(usuario,lista):
        #adiciona o usuario na lista de usuarios bloqueados
        lista.push(usuario)