from business.commands.Command import Command

class ListAllCursosCommand(Command):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        self.controller.listAll()