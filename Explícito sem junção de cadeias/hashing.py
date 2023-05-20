import sys

#-----------------------Função de Inserção-------------------------------
def insertion(hashTable, point):
#Variavés de controle
	posLivre = len(hashTable)-1
	qntInteiros = 1 
	aux=0
	
#inserção
	while(qntInteiros < len(inteiros)):
		o=0
		aux = int(inteiros[qntInteiros]%inteiros[0])
		if hashTable[aux] == "vazio":
			hashTable[aux] = int(inteiros[qntInteiros])
		elif hashTable[aux]%inteiros[0] != aux:
			#aloca o registro de acordo com o hashing e realoca o que estava na posição
			value = hashTable[aux]
			hashTable[aux] = int(inteiros[qntInteiros])
			#verifica a posição do apontador
			if posLivre != -1:
				hashTable[posLivre] = int(value)
				point[posLivre] = point[aux]
				point[aux] = 'vazio'
				count = 0

				while (count <= inteiros[0]):
					if( point[count] == aux):
						point[count] = posLivre 
						break
					count += 1
				while (hashTable[posLivre] != "vazio" and posLivre > 0):
					posLivre -=1
				if posLivre < 0:
					print("arquivo cheio!")
					break


		elif posLivre != -1:
			if hashTable[posLivre] == 'vazio':
				hashTable[posLivre] = int(inteiros[qntInteiros])
			else:
				while (hashTable[posLivre] != "vazio"):
					posLivre -=1
					if(posLivre<0):
						print("arquivo cheio!")
						break
				hashTable[posLivre] = int(inteiros[qntInteiros])
				
			#Atualização da tabela dos apontadores
			while(o<1):
				if point[aux] == "vazio":
					point[aux] = int(posLivre)
					o+=1
				else:
					aux = point[aux]
			#Mudar o apontador para a próxima posição livre do arquivo		
			while (hashTable[posLivre] != "vazio"):
				posLivre -=1
				if(posLivre<0):
					print("arquivo cheio!")
					break
		qntInteiros +=1

#consulta
def search(hashTable, inteiros, point):
	acessos = 0
	for num in inteiros[1:]:
		hash = num%inteiros[0]
		acessos += 1
		if hashTable[hash] == num:
			continue
		else:
			aux = hash
			while hashTable[aux] != num and hashTable[aux] != 'vazio':
				acessos += 1
				if point[aux] != 'vazio':
					aux = point[aux]
					if hashTable[aux] == num:
						continue
				else:
					break	
	print(acessos/(len(inteiros)- 1))



#-----------------------Função Principal-------------------------------
#inicialização das listas e variavéis que serão utilizadas
inteiros = []
hashTable = []
point = []
cont = 0
contagem = 0

if len(sys.argv) > 1:
	inFile = sys.argv[1]
	with open(inFile,'r') as i:
		lines = i.read().splitlines()
		for num in lines:
			inteiros.append(int(num))
else:
	print("Insira o tamanho da tabela Hashing: ")
	table_size = int(input())
	inteiros.append(table_size)
	print("Digite os elementos a serem inseridos: ")
	while True:
		try:
			inteiros.append(int(input()))
		except:
			break
	

# Preenchimento da tabela Hashing e da tabela dos apontadores
while (cont<inteiros[0]):
	hashTable.append("vazio")
	point.append("vazio")
	cont +=1
	

insertion(hashTable, point)


print("Tabela hashing após o processo:")
print(hashTable)
print("-----------------------------------------------------------------------")
print("Tabela de apontadores após o processo:")
print(point)
print("Número médio de acessos")
search(hashTable, inteiros, point)
