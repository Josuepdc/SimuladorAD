# coding: latin1
'''
Autores: Felipe Casto, Gabriel Matos, Josu� Pereira e Julia Anne
Trabalho Final de AD 2016
'''
import random, time
import utils

'''=========================== Parametros iniciais =========================== '''
lambda1 = 1/5
lambda2 = 1/5
numeroIteracoes = 2000
numeroRodadas = 10
escalonamento = "FCFS"

'''=========================== Metricas de Interesse ======================== '''
W = []
X1 = []
X2 = []
N1 = []
N2 = []

'''============================== Inicializacao ============================= '''
fila = utils.Fila(escalonamento)
servidor = utils.Servidor()


for j in range(numeroRodadas):
	print (50*'-')
	print ("RODADA ", j)
	print (50*'-')
	fila.reset()
	servidor.reset()
	contadorIds = 0
	tempoAteProximaChegada = 0
	trabalhoNoServidor = 0
	tempoDeSaida = 0
	x1_temp = 0
	x2_temp = 0
	n1_temp = 0
	n2_temp = 0
	w_temp = 0
	n_saidas = 0
	total1 = 0
	total2 = 0
	totalServico1 = 0
	totalServico2 = 0
	tempoUltimaSaida = 0
	proximoClasse1 = random.expovariate(lambda1)
	proximoClasse2 = random.expovariate(lambda2)
	print ("O proximo da Classe 1: ", proximoClasse1)
	print ("O proximo da Classe 2: ", proximoClasse2)

	if proximoClasse1 < proximoClasse2:
		tempoAteProximaChegada += proximoClasse1
		print("Tempo ate a proxima chegada e: ", tempoAteProximaChegada, " e sera da classe 1")
	else:
		tempoAteProximaChegada += proximoClasse2
		print("Tempo ate a proxima chegada e: ", tempoAteProximaChegada, " e sera da classe 2")
	contadorIds += 1
	print(50*'-')
	for i in range(numeroIteracoes): #antigoWhileTrue

		if (tempoAteProximaChegada < tempoDeSaida):
			if proximoClasse1 < proximoClasse2:
				fila.addFila(utils.Job(1, tempoAteProximaChegada, random.uniform(1,3), contadorIds))
				print("Job ", contadorIds, " da classe 1 entrou na fila")
			else:
				fila.addFila(utils.Job(2, tempoAteProximaChegada, random.uniform(1,3), contadorIds))
				print("Job ", contadorIds, " da classe 2 entrou na fila")
			tam = fila.getTamanhoFila()
			print ("Tamanho da Fila: ", tam)
		else:
			while tempoDeSaida != 0:
				print("Job ", servidor.getJob().getID(), " terminou")
				w_temp += tempoDeSaida - servidor.getJob().getTempoChegada()
				n_saidas += 1
				tempoUltimaSaida = tempoDeSaida
				servidor.setJob(None)
				if fila.getTamanhoFila() == 0 and proximoClasse1 < proximoClasse2:
					fila.addFila(utils.Job(1, tempoAteProximaChegada, random.uniform(1,3), contadorIds))
					print("Job ", contadorIds, " da classe 1 entrou na fila")
				elif fila.getTamanhoFila() == 0 and proximoClasse1 > proximoClasse2:
					fila.addFila(utils.Job(2, tempoAteProximaChegada, random.uniform(1,3), contadorIds))
					print("Job ", contadorIds, " da classe 2 entrou na fila")
				proxJob = fila.getProximoDaFila()
				if proxJob != None:
					servidor.setJob(proxJob)
					job = servidor.getJob()
					print("Job ", job.getID(), " entrou em servico")
					tempoJob = job.getTempoDeServico()
					trabalhoNoServidor = tempoJob
					tam = fila.getTamanhoFila()
					print("Tempo de servico: ", tempoJob)
					print("Classe: ", job.getClasse())
					if job.getClasse() == 1:
						x1_temp += tempoJob
						totalServico1 += 1
					else:
						x2_temp += tempoJob
						totalServico2 += 1
					print ("Tamanho da Fila: ", tam)
					if tam < 1:
						tempoDeSaida = tempoAteProximaChegada + tempoJob
						print("Tempo de saida do Job ", job.getID(), ": ", tempoDeSaida)
					else:
						tempoDeSaida += tempoJob
						print("Tempo de ## saida do Job ", job.getID(), ": ", tempoDeSaida)
				#if tempoAteProximaChegada < tempoDeSaida:
					#tempoDeSaida = 0
				print(50*'-')
				tam = fila.getTamanhoFila()
				print ("Tamanho da Fila: ", tam)
				break

			else:#primeiroJobNoServidor
				if (proximoClasse1 < proximoClasse2):
					fila.addFila(utils.Job(1, tempoAteProximaChegada, random.uniform(1,3), contadorIds))
					print("Job ", contadorIds, " da classe 1 entrou na fila")
				else:
					fila.addFila(utils.Job(2, tempoAteProximaChegada, random.uniform(1,3), contadorIds))
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
			proximoClasse1 = proximoClasse1 + random.expovariate(lambda1)
		else:
			proximoClasse2 = proximoClasse2 + random.expovariate(lambda2)

		if (proximoClasse1 < proximoClasse2):
			tempoAteProximaChegada =+ proximoClasse1
		else:
			tempoAteProximaChegada =+ proximoClasse2


		print ("O proximo da Classe 1: ", proximoClasse1)
		print ("O proximo da Classe 2: ", proximoClasse2)
		print(50*'-')
		print("Tempo ate a proxima chegada: ", tempoAteProximaChegada)
		contadorIds += 1
	while fila.getTamanhoFila() != 0:
		print("Job ", servidor.getJob().getID(), " terminou")
		w_temp += tempoDeSaida - servidor.getJob().getTempoChegada()
		n_saidas += 1
		tempoUltimaSaida = tempoDeSaida
		servidor.setJob(None)
		proxJob = fila.getProximoDaFila()
		if proxJob != None:
			servidor.setJob(proxJob)
			job = servidor.getJob()
			print("Job ", job.getID(), " entrou em servico")
			tempoJob = job.getTempoDeServico()
			trabalhoNoServidor = tempoJob
			tam = fila.getTamanhoFila()
			print("Tempo de servico: ", tempoJob)
			print("Classe: ", job.getClasse())
			if job.getClasse() == 1:
				x1_temp += tempoJob
				totalServico1 += 1
			else:
				x2_temp += tempoJob
				totalServico2 += 1
			print ("Tamanho da Fila: ", tam)
			if tam < 1:
				tempoDeSaida = tempoAteProximaChegada + tempoJob
				print("Tempo de saida do Job ", job.getID(), ": ", tempoDeSaida)
			else:
				tempoDeSaida += tempoJob
				print("Tempo de ## saida do Job ", job.getID(), ": ", tempoDeSaida)
		print(50*'-')
	W.append(w_temp/n_saidas)
	X1.append(x1_temp/totalServico1)
	X2.append(x2_temp/totalServico2)
X = ((lambda1/(lambda1+lambda2)) * sum(X1)/numeroRodadas) + ((lambda1/(lambda1+lambda2)) * sum(X2)/numeroRodadas)
print ("E[T]: ", sum(W)/numeroRodadas + X)
print("E[N]: ", (lambda1+lambda2)*(sum(W)/numeroRodadas + X))
print("E[X]: ", X)
