# coding: latin1
'''
Autores: Felipe Casto, Gabriel Matos, Josu� Pereira e Julia Anne
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
						raise Exception('Escalonamento n�o definido !!!')
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
