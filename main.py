# coding: latin1
'''
Autores: Felipe Casto, Gabriel Matos, Josu� Pereira e Julia Anne
Trabalho Final de AD 2016
'''
import random
import utils

if __name__ == '__main__':
	'''=========================== INICIALIZA��O =========================== '''
	lambda1 = 10
	lambda2 = 15
	mu1 = 20
	mu2 = 15
	T = 0
	contadorIds = 1
	escalonamento = "FCFS"

	'''=========================== CODIGO =========================== '''
	fila = utils.Fila(escalonamento)
	servidor = utils.Servidor(mu1, mu2)


	proximoClasse1 = random.expovariate(lambda1)
	proximoClasse2 = random.expovariate(lambda2)


	while True:
		if (proximoClasse1 < proximoClasse2):
			fila.addFila(utils.Job(1, contadorIds))
			contadorIds += 1
			proximoClasse1 = random.expovariate(lambda1)
		elif (proximoClasse1 > proximoClasse2):
			fila.addFila(utils.Job(2, contadorIds))
			contadorIds += 1
			proximoClasse2 = random.expovariate(lambda2)
