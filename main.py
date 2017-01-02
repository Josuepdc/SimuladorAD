# coding: latin1
'''
Autores: Felipe Casto, Gabriel Matos, Josué Pereira e Julia Anne
Trabalho Final de AD 2016
'''
import random

class Job:
    def __init__(self, classe, id):
        self.classe = classe        
        self.trabalhoResidual = 0
        self.ID = id

    def setTrabalhoResidual(self, trabalhoResidual):
        self.trabalhoResidual = trabalhoResidual

    def getTrabalhoResidual(self):
        return self.trabalhoResidual

    def getClasse(self):
        return self.classe

    def getID(self):
        return self.ID



class Fila:
    '''Classe definida para organizar a tratar a fila de Jobs'''
    def __init__(self, escalonamento):
        self.fila = []
        self.escalonamento = escalonamento
        if self.escalonamento != "FCFS" and self.escalonamento != "LCFS":
            raise Exception('Escalonamento não definido !!!')
        self.contadorClasse1 = 0
        self.contadorClasse2 = 0

    def getProximoDaFila(self):
        if self.escalonamento == "FCFS":
            return self.fila.pop(0)
        elif self.escalonamento == "LCFS":
            return self.fila.pop(len(self.fila)-1)

    def addFila(self, job):
        self.fila.append(job)

    def getFila(self):
        return self.fila




class Servidor:
    def __init__(self, mu1, mu2):
        self.mu1 = mu1
        self.mu2 = mu2
        self.tempoNoServidor = 0
        self.job = None

    def setTempoNoServidor(self, job):
        if job.getClasse() == 1:
            tempoNoServidor = random.expovariate(mu1)
        else:
            tempoNoServidor = random.expovariate(mu2)
    
    def getTempoNoServidor(self):
        return self.tempoNoServidor

    def getJob(self):
        return self.job

    def setJob(self, job):
        self.job = job






if __name__ == '__main__':
    '''=========================== INICIALIZAÇÃO =========================== '''
    lambda1 = 10
    lambda2 = 15
    mu1 = 20
    mu2 = 15
    T = 0
    contadorIds = 1
    escalonamento = "FCFS"

    '''=========================== CODIGO =========================== '''
    fila = Fila(escalonamento)
    servidor = Servidor(mu1, mu2)


    proximoClasse1 = random.expovariate(lambda1)
    proximoClasse2 = random.expovariate(lambda2)


    while True:
        if (proximoClasse1 < proximoClasse2):
            fila.addFila(Job(1, contadorIds))
            contadorIds += 1
            proximoClasse1 = random.expovariate(lambda1)
        elif (proximoClasse1 > proximoClasse2):
            fila.addFila(Job(2, contadorIds))
            contadorIds += 1
            proximoClasse2 = random.expovariate(lambda2)