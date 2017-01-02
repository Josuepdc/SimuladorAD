# coding: latin1

'''
Autores: Felipe Casto, Gabriel Matos, Josué Pereira e Julia Anne
Trabalho Final de AD 2016
'''

import random
import threading
import time

class Job:
    def __init__(self, classe):
        self.classe = classe        
        self.trabalhoResidual = 0

    def __repr__(self):
        return "Classe: " + str(self.classe)

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


def chegadaJob(classe, taxa, fila):
    while 1:
        time.sleep(random.expovariate(2))
        fila.addFila(Job(classe))



if __name__ == '__main__':
    fila = Fila("FCFS")
    
    threading.Thread(target=chegadaJob, args=(1, 2, fila)).start()
    threading.Thread(target=chegadaJob, args=(2, 10, fila)).start()
