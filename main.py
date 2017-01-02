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
    def __init__(self, escalonamento):
        self.fila = []
        self.escalonamento = escalonamento
        if self.escalonamento != "FCFS" and self.escalonamento != "LCFS":
            raise Exception('Escalonamento não definido !!!')    

    def getProximoDaFila(self):
        if self.escalonamento == "FCFS":
            return self.fila.pop(0)
        elif self.escalonamento == "LCFS":
            return self.fila.pop(len(self.fila)-1)

    def addFila(self, job):
        self.fila.append(job)







class Servidor:
    pass



if __name__ == '__main__':
    fila = Fila("FCFS")
