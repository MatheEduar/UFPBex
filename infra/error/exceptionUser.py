class ExceptionUser(Exception):
    def __init__(self, mensagem="Usuário Inválido!"):
        super().__init__(mensagem)