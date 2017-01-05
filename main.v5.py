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
	lambda2 = 5
	mu = 20
	# mu2 = 15
	tempoAteProximaChegada = 0
	trabalhoNoServidor = 0
	tempoDeSaida = 0

	contadorIds = 0
	escalonamento = "FCFS"

	'''=========================== CODIGO =========================== '''
	fila = utils.Fila(escalonamento)
	servidor = utils.Servidor()

	'''======================= Inicializacao ======================== '''
	proximoClasse1 = random.expovariate(1/lambda1)
	proximoClasse2 = random.expovariate(1/lambda2)

	print ("***** Classe 1: ", proximoClasse1)
	print ("***** Classe 2: ", proximoClasse2)

	if (proximoClasse1 < proximoClasse2) :
		tempoAteProximaChegada += proximoClasse1
		print(50*'-')
		print("Tempo ate a proxima chegada: ", tempoAteProximaChegada, " e é da classe 1")
	else:
		tempoAteProximaChegada += proximoClasse2
		print(50*'-')
		print("Tempo ate a proxima chegada: ", tempoAteProximaChegada, " e é da classe 2")
	contadorIds += 1


	while True:
		if (tempoAteProximaChegada < tempoDeSaida):
			if (proximoClasse1 < proximoClasse2):
				if (servidor.getJob().getClasse() == 2):
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
					fila.addFila(utils.Job(1, random.uniform(10,30), contadorIds))
					print("Job ", contadorIds, " entrou na fila e é da classe 1")
			else:
				fila.addFila(utils.Job(2, random.uniform(10,30), contadorIds))
				print("Job ", contadorIds, " entrou na fila e é da classe 2")
			tam = fila.getTamanhoFila()
			print ("Tamanho da Fila: ", tam)

		else:
			while tempoDeSaida != 0:
				print("Job ", servidor.getJob().getID(), " terminou")
				servidor.setJob(None)
				if fila.getTamanhoFila() != 0:
					if fila.getClassQuantidade(1) > 0:
						for i in range(fila.getTamanhoFila()):
							if fila.fila[i].getClasse() == 1:
								servidor.setJob(fila.getElementoDaFila(i))
								job = servidor.getJob()
								print("Job ", job.getID(), " entrou em servico")
								tempoJob = job.getTempoDeServico()
								trabalhoNoServidor = tempoJob
								tam = fila.getTamanhoFila()
								print("Tempo de servico: ", tempoJob)
								print("Classe: ", job.getClasse())
								break
					else:
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
					if (proximoClasse1 < proximoClasse2):
						if (servidor.getJob().getClasse() == 2):
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
							fila.addFila(utils.Job(1, random.uniform(10,30), contadorIds))
							print("Job ", contadorIds, " entrou na fila e é da classe 1")
					else:
						fila.addFila(utils.Job(2, random.uniform(10,30), contadorIds))
						print("Job ", contadorIds, " entrou na fila e é da classe 2")
					tam = fila.getTamanhoFila()
					print ("Tamanho da Fila: ", tam)
					break
			else: #caso start
				if (proximoClasse1 < proximoClasse2):
					fila.addFila(utils.Job(1, random.uniform(10,30), contadorIds))
					print("Job ", contadorIds, " entrou na fila e é da classe 1")
				else:
					fila.addFila(utils.Job(2, random.uniform(10,30), contadorIds))
					print("Job ", contadorIds, " entrou na fila e é da classe 2")
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

		print ("***** Classe 1A: ", proximoClasse1)
		print ("***** Classe 2A: ", proximoClasse2)

		print(50*'-')
		print("Tempo ate a proxima chegada: ", tempoAteProximaChegada)
		contadorIds += 1
