# coding: latin1
'''
Autores: Felipe Casto, Gabriel Matos, Josu� Pereira e Julia Anne
Trabalho Final de AD 2016
'''
import random, time
import utils

'''=========================== Parametros iniciais =========================== '''
lambda1 = 20
lambda2 = 20
numeroIteracoes = 100
tempoAteProximaChegada = 0
trabalhoNoServidor = 0
tempoDeSaida = 0
contadorIds = 0
escalonamento = "LCFS"
'''============================== Inicializacao ============================= '''
fila = utils.Fila(escalonamento)
servidor = utils.Servidor()

proximoClasse1 = random.expovariate(1/lambda1)
proximoClasse2 = random.expovariate(1/lambda2)
print ("O proximo da Classe 1: ", proximoClasse1)
print ("O proximo da Classe 2: ", proximoClasse2)

if (proximoClasse1 < proximoClasse2) :
	tempoAteProximaChegada += proximoClasse1
	print(50*'-')
	print("Tempo ate a proxima chegada da classe 1: ", tempoAteProximaChegada)
else:
	tempoAteProximaChegada += proximoClasse2
	print(50*'-')
	print("Tempo ate a proxima chegada da classe 2: ", tempoAteProximaChegada)
contadorIds += 1


for i in range(numeroIteracoes):#antigoWhileTrue
	
	if (tempoAteProximaChegada < tempoDeSaida):
		if (proximoClasse1 < proximoClasse2):
			if (servidor.getJob() != None):
				print ("O Job ", servidor.getJob().getID(), " foi retirado do servidor")
				jobServidor = servidor.getJob()
				jobServidor.setTrabalhoResidual(tempoDeSaida - tempoAteProximaChegada)
				fila.addFila(servidor.getJob())
			servidor.setJob(utils.Job(1, random.uniform(10,30), contadorIds))
			job = servidor.getJob()
			print("Job ", job.getID(), " entrou em servico")
			tempoJob = job.getTempoDeServico()
			tempoDeSaida = tempoAteProximaChegada + tempoJob
			tam = fila.getTamanhoFila()
			print("Tempo de servico: ", tempoJob)
			print("Tempo de saida do Job ", job.getID(), ": ", tempoDeSaida)
			print("Classe: ", job.getClasse())
		else:
			if (servidor.getJob() != None):
				print ("O Job ", servidor.getJob().getID(), " foi retirado do servidor")
				jobServidor = servidor.getJob()
				jobServidor.setTrabalhoResidual(tempoDeSaida - tempoAteProximaChegada)
				fila.addFila(servidor.getJob())
			servidor.setJob(utils.Job(2, random.uniform(10,30), contadorIds))
			job = servidor.getJob()
			print("Job ", job.getID(), " entrou em servico")
			tempoJob = job.getTempoDeServico()
			tempoDeSaida = tempoAteProximaChegada + tempoJob
			tam = fila.getTamanhoFila()
			print("Tempo de servico: ", tempoJob)
			print("Tempo de saida do Job ", job.getID(), ": ", tempoDeSaida)
			print("Classe: ", job.getClasse())
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
				tempoJob = job.getTrabalhoResidual()
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
				if (proximoClasse1 < proximoClasse2):
					if (servidor.getJob() != None):
						print ("O Job ", servidor.getJob().getID(), " foi retirado do servidor")
						jobServidor = servidor.getJob()
						jobServidor.setTrabalhoResidual(tempoDeSaida - tempoAteProximaChegada)
						fila.addFila(servidor.getJob())
					servidor.setJob(utils.Job(1, random.uniform(10,30), contadorIds))
					job = servidor.getJob()
					print("Job ", job.getID(), " entrou em servico")
					tempoJob = job.getTempoDeServico()
					tempoDeSaida = tempoAteProximaChegada + tempoJob
					tam = fila.getTamanhoFila()
					print("Tempo de servico: ", tempoJob)
					print("Tempo de saida do Job ", job.getID(), ": ", tempoDeSaida)
					print("Classe: ", job.getClasse())
				else:
					if (servidor.getJob() != None):
						print ("O Job ", servidor.getJob().getID(), " foi retirado do servidor")
						jobServidor = servidor.getJob()
						jobServidor.setTrabalhoResidual(tempoDeSaida - tempoAteProximaChegada)
						fila.addFila(servidor.getJob())
					servidor.setJob(utils.Job(2, random.uniform(10,30), contadorIds))
					job = servidor.getJob()
					print("Job ", job.getID(), " entrou em servico")
					tempoJob = job.getTempoDeServico()
					tempoDeSaida = tempoAteProximaChegada + tempoJob
					tam = fila.getTamanhoFila()
					print("Tempo de servico: ", tempoJob)
					print("Tempo de saida do Job ", job.getID(), ": ", tempoDeSaida)
					print("Classe: ", job.getClasse())
				tam = fila.getTamanhoFila()
				print ("Tamanho da Fila: ", tam)
				break

		else:#primeiroJobNoServidor
			if (proximoClasse1 < proximoClasse2):
				servidor.setJob(utils.Job(1, random.uniform(10,30), contadorIds))
				job = servidor.getJob()
				print("Job ", job.getID(), " entrou em servico")
				tempoJob = job.getTempoDeServico()
				tempoDeSaida = tempoAteProximaChegada + tempoJob
				tam = fila.getTamanhoFila()
				print("Tempo de servico: ", tempoJob)
				print("Tempo de saida do Job ", job.getID(), ": ", tempoDeSaida)
				print("Classe: ", job.getClasse())
			else:
				servidor.setJob(utils.Job(2, random.uniform(10,30), contadorIds))
				job = servidor.getJob()
				print("Job ", job.getID(), " entrou em servico")
				tempoJob = job.getTempoDeServico()
				tempoDeSaida = tempoAteProximaChegada + tempoJob
				tam = fila.getTamanhoFila()
				print("Tempo de servico: ", tempoJob)
				print("Tempo de saida do Job ", job.getID(), ": ", tempoDeSaida)
				print("Classe: ", job.getClasse())
			tam = fila.getTamanhoFila()
			print ("Tamanho da Fila: ", tam)


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