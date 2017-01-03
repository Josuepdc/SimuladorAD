# coding: latin1
'''
Autores: Felipe Casto, Gabriel Matos, Josu� Pereira e Julia Anne
Trabalho Final de AD 2016
'''
import random, time
import utils

if __name__ == '__main__':
	'''=========================== INICIALIZA��O =========================== '''
	lambda1 = 5
	lambda2 = 15
	mu = 20
	# mu2 = 15
	T = 0
	trabalhoNoServidor = 0

	contadorIds = 0
	escalonamento = "FCFS"

	'''=========================== CODIGO =========================== '''
	fila = utils.Fila(escalonamento)
	servidor = utils.Servidor(mu)

	while True:
		proximoClasse1 = random.expovariate(1/lambda1)
		T += proximoClasse1
		print("Proxima chegada: ", T)
		contadorIds += 1
		fila.addFila(utils.Job(1, random.uniform(0,2), contadorIds))
		tam = fila.getTamanhoFila()
		print ("Tamanho da Fila: ", tam)
		if servidor.getJob() == None:
			servidor.setJob(fila.getProximoDaFila())
			job = servidor.getJob()
			tempoJob = job.getTempoDeServico()
			trabalhoNoServidor = tempoJob
			print("Tempo de servico: ", tempoJob)
			print("Classe: ", job.getClasse())
		else:
			trabalhoNoServidor -= taxa
	# proximoClasse2 = random.expovariate(1/lambda2)


	# while True:
	# 	if (proximoClasse1 < proximoClasse2):
	# 		fila.addFila(utils.Job(1, contadorIds))
	# 		contadorIds += 1
	# 		proximoClasse1 = random.expovariate(lambda1)
	# 	elif (proximoClasse1 > proximoClasse2):
	# 		fila.addFila(utils.Job(2, contadorIds))
	# 		contadorIds += 1
	# 		proximoClasse2 = random.expovariate(lambda2)
