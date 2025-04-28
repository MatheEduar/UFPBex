class ExceptionPassword(Exception):
    def __init__(self, mensagem="Senha Inválida!"):
        super().__init__(mensagem)