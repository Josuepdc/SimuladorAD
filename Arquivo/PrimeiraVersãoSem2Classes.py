# coding: latin1
'''
Autores: Felipe Casto, Gabriel Matos, Josu� Pereira e Julia Anne
Trabalho Final de AD 2016
'''
import random, time
import utils

if __name__ == '__main__':
	'''=========================== Parametros iniciais =========================== '''
	lambda1 = 5
	lambda2 = 15
	mu = 20
	# mu2 = 15
	tempoAteProximaChegada = 0
	trabalhoNoServidor = 0
	tempoDeSaida = 0

	contadorIds = 0
	# escalonamento = "FCFS"
	escalonamento = "LCFS"

	'''=========================== CODIGO =========================== '''
	fila = utils.Fila(escalonamento)
	servidor = utils.Servidor()

	'''======================= Inicializacao ======================== '''
	proximoClasse1 = random.expovariate(1/lambda1)
	# proximoClasse2 = random.expovariate(1/lambda2)
	# if proximoClasse1 < proximoClasse2
	# 	tempoAteProximaChegada += proximoClasse1
	print(50*'-')
	print("Tempo ate a proxima chegada: ", tempoAteProximaChegada)
	contadorIds += 1
	# tempoDeSaida = tempoAteProximaChegada + job.getTempoDeServico()
	# print("Tempo de saida do Job ", job.getID(), ": ", tempoDeSaida)


	while True:
		# if tempoDeSaida > 0:
		if tempoAteProximaChegada < tempoDeSaida:
			fila.addFila(utils.Job(1, random.uniform(10,30), contadorIds))
			print("Job ", contadorIds, " entrou na fila")
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
				if tempoAteProximaChegada < tempoDeSaida:
					print(50*'-')
					fila.addFila(utils.Job(1, random.uniform(10,30), contadorIds))
					print("Job ", contadorIds, " entrou na fila")
					tam = fila.getTamanhoFila()
					print ("Tamanho da Fila: ", tam)
					break
			else:
				job = utils.Job(1, random.uniform(10,30), contadorIds)
				fila.addFila(job)
				print("Job ", contadorIds, " entrou na fila")
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

		proximoClasse1 = random.expovariate(1/lambda1)
		tempoAteProximaChegada += proximoClasse1
		print(50*'-')
		print("Tempo ate a proxima chegada: ", tempoAteProximaChegada)
		contadorIds += 1












		# else:
		# 	fila.addFila(utils.Job(1, random.uniform(10,30), contadorIds))
		# 	servidor.setJob(fila.getProximoDaFila())
		# 	job = servidor.getJob()
		# 	tempoJob = job.getTempoDeServico()
		# 	trabalhoNoServidor = tempoJob
		# 	tam = fila.getTamanhoFila()
		# 	print("Tempo de servico: ", tempoJob)
		# 	print("Classe: ", job.getClasse())
		# 	print ("Tamanho da Fila: ", tam)


		# tam = fila.getTamanhoFila()
		# print ("Tamanho da Fila: ", tam)
		# if servidor.getJob() == None:
		# 	servidor.setJob(fila.getProximoDaFila())
		# 	job = servidor.getJob()
		# 	tempoJob = job.getTempoDeServico()
		# 	trabalhoNoServidor = tempoJob
		# 	tam = fila.getTamanhoFila()
		# 	print("Tempo de servico: ", tempoJob)
		# 	print("Classe: ", job.getClasse())
		# 	if tam < 1:
		# 		tempoDeSaida = tempoAteProximaChegada + tempoJob
		# 		print(tempoDeSaida)
		# 	else:
		# 		tempoDeSaida += tempoJob

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
