# coding: latin1
'''
Autores: Felipe Casto, Gabriel Matos, Josu� Pereira e Julia Anne
Trabalho Final de AD 2016
'''
import random, time
import utils

'''=========================== Parametros iniciais =========================== '''
lambda1 = 5
lambda2 = 5
numeroIteracoes = 100
tempoAteProximaChegada = 0
trabalhoNoServidor = 0
tempoDeSaida = 0
contadorIds = 0
escalonamento = "FCFS"
'''============================== Inicializacao ============================= '''
fila = utils.Fila(escalonamento)
servidor = utils.Servidor()

proximoClasse1 = random.expovariate(1/lambda1)
proximoClasse2 = random.expovariate(1/lambda2)
print ("O proximo da Classe 1: ", proximoClasse1)
print ("O proximo da Classe 2: ", proximoClasse2)

if (proximoClasse1 < proximoClasse2) :
	tempoAteProximaChegada += proximoClasse1
	print("Tempo ate a proxima chegada é: ", tempoAteProximaChegada, " e será da classe 1")
else:
	tempoAteProximaChegada += proximoClasse2
	print("Tempo ate a proxima chegada é: ", tempoAteProximaChegada, " e será da classe 2")
contadorIds += 1
print(50*'-')

for i in range(numeroIteracoes): #antigoWhileTrue
	
	if (tempoAteProximaChegada < tempoDeSaida):
		if (proximoClasse1 < proximoClasse2):
			fila.addFila(utils.Job(1, random.uniform(10,30), contadorIds))
			print("Job ", contadorIds, " da classe 1 entrou na fila")
		else:
			fila.addFila(utils.Job(2, random.uniform(10,30), contadorIds))
			print("Job ", contadorIds, " da classe 2 entrou na fila")
		tam = fila.getTamanhoFila()
		print ("Tamanho da Fila: ", tam)
	else:
		while tempoDeSaida != 0:
			print("Job ", servidor.getJob().getID(), " terminou")
			servidor.setJob(None)
			if fila.getTamanhoFila() != 0:
				servidor.setJob(fila.getProximoDaFila())
				job = servidor.getJob()
				print("Job ", job.getID(), " entrou em servico")
				tempoJob = job.getTempoDeServico()
				trabalhoNoServidor = tempoJob
				tam = fila.getTamanhoFila()
				print("Tempo de servico: ", tempoJob)
				print("Classe: ", job.getClasse())
			print ("Tamanho da Fila: ", tam)
			if tam < 1:
				tempoDeSaida = tempoAteProximaChegada + tempoJob
				print("Tempo de saida do Job ", job.getID(), ": ", tempoDeSaida)
			else:
				tempoDeSaida += tempoJob
				print("Tempo de saida do Job ", job.getID(), ": ", tempoDeSaida)
			if (tempoAteProximaChegada < tempoDeSaida):
				print(50*'-')
				if (proximoClasse1 < proximoClasse2):
					fila.addFila(utils.Job(1, random.uniform(10,30), contadorIds))
					print("Job ", contadorIds, " da classe 1 entrou na fila")
				else:
					fila.addFila(utils.Job(2, random.uniform(10,30), contadorIds))
					print("Job ", contadorIds, " da classe 2 entrou na fila")
				tam = fila.getTamanhoFila()
				print ("Tamanho da Fila: ", tam)
				break

		else:#primeiroJobNoServidor
			if (proximoClasse1 < proximoClasse2):
				fila.addFila(utils.Job(1, random.uniform(10,30), contadorIds))
				print("Job ", contadorIds, " da classe 1 entrou na fila")
			else:
				fila.addFila(utils.Job(2, random.uniform(10,30), contadorIds))
				print("Job ", contadorIds, " da classe 2 entrou na fila")
			servidor.setJob(fila.getProximoDaFila())
			job = servidor.getJob()
			print("Job ", job.getID(), " entrou em servico")
			tempoJob = job.getTempoDeServico()
			trabalhoNoServidor = tempoJob
			tam = fila.getTamanhoFila()
			print("Tempo de servico: ", tempoJob)
			print("Classe: ", job.getClasse())
			tempoDeSaida = tempoAteProximaChegada + tempoJob
			print("Tempo de saida do Job ", job.getID(), ": ", tempoDeSaida)


	if (proximoClasse1 < proximoClasse2):
		proximoClasse1 = proximoClasse1 + random.expovariate(1/lambda1)
	else:
		proximoClasse2 = proximoClasse2 + random.expovariate(1/lambda2)

	if (proximoClasse1 < proximoClasse2):
		tempoAteProximaChegada =+ proximoClasse1
	else:
		tempoAteProximaChegada =+ proximoClasse2


	print ("O proximo da Classe 1: ", proximoClasse1)
	print ("O proximo da Classe 2: ", proximoClasse2)
	print(50*'-')
	print("Tempo ate a proxima chegada: ", tempoAteProximaChegada)
	contadorIds += 1