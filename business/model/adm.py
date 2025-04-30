from model.user import User

class Adm(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def listar_usuarios(self, controller):
        controller.listAll()

    def bloquear_usuario(self, controller, username):
        user = controller.listUser(username)
        if user:

            print(f"Usuário {username} bloqueado.")
        else:
            print("Usuário não encontrado.")