def cadastrar_Usuario(lista):
    nome = input("Digite o nome do usuario: ")
    nick = input("Digite o nome de usuario: ")
    email = input("Digite o email do usuario: ")
    senha = input("Digite a senha do usuario: ")
    usuario = usuario.Usuario()
    usuario.nome = nome
    usuario.username = nick
    usuario.email = email
    usuario.senha = senha
    lista.push(usuario)
    
def editar_Usuario(usuario):
    #todo
    pass
    
            
    

usuarios_cadastrados = []
cadastrar_Usuario(usuarios_cadastrados)