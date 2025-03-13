from error import dataException
class UserPersistence():
    def __init__(self,file):
        self.file = file
    
    def loadUsers(self):
        data_list= []
    
        with open(self.file, 'r') as file:
            for line in file:
                data = line.strip().split()
                data_list.append(tuple(data))
        return data_list
    
    def saveUsers(self,lista):
        #TODO metodo que salva novos usuarios cadastrados no arquivo 
        #TODO (cuidado para não salvar usuarios já existentes duas vezes) 
        pass
            