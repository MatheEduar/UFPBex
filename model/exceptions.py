class InvalidUsernameException(Exception):
    def __init__(self, mensagem="Entrada inválida!"):
        super().__init__(mensagem)

class InvalidPasswordException(Exception):
    def __init__(self, mensagem="Entrada inválida!"):
        super().__init__(mensagem)