class CursoCaretaker:
    def __init__(self, curso_dao):
        self._mementos = []
        #self._mementos_redo = []
        self._curso_dao = curso_dao

    def backup(self):
        print("Caretaker: Salvando estado dos cursos...")
        self._mementos.append(self._curso_dao.save_to_memento())

    def undo(self):
        if not self._mementos:
            return

        memento = self._mementos.pop()
        print("Caretaker: Restaurando estado dos cursos...")
        self._curso_dao.restore_from_memento(memento)

    # def redo(self):
    #     if self._mementos_redo:
    #         memento = self._mementos_redo.pop()
    #         print("Caretaker: Refazendo estado dos cursos...")
    #         self._curso_dao.restore_from_memento(memento)
    #         self._mementos.append(memento)