# coding: latin1

'''
Autores: Felipe Casto, Gabriel Matos, Josué Pereira e Julia Anne
Trabalho Final de AD 2016
'''

class Jobs:
    def __init__(self, classe):
        self.classe = classe        
        self.trabalhoResidual = 0

    def setTrabalhoResidual(self, trabalhoResidual):
        self.trabalhoResidual = trabalhoResidual

    def getTrabalhoResidual(self):
        return self.trabalhoResidual

    def getClasse(self):
        return self.classe





class Fila:
    '''Classe definida para organizar a tratar a fila de Jobs'''
    def __init__(self, scheduling):
        self.queue = []
        self.scheduling = scheduling
        if self.scheduling != "FCFS" and self.scheduling != "LCFS":
            raise Exception('Escalonamento não definido !!!')    

    def getQueue(self):
        if self.scheduling == "FCFS":
            return self.queue.pop(0)
        elif self.scheduling == "LCFS":
            return self.queue.pop(len(self.queue)-1)

    def addQueue(self, job):
        self.queue.append(job)







class Server:
    pass



if __name__ == '__main__':
    fila = Fila("FCFS")
