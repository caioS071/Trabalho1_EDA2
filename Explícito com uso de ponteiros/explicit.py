
#-----------------------Função de Inserção-------------------------------
def insertion(hashTable, point, contagem):
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
			contagem+=1

		elif posLivre != -1:
			hashTable[posLivre] = int(inteiros[qntInteiros])
			#Atualização da tabela dos apontadores
			contagem+=1
			while(o<1):
				if point[aux] == "vazio":
					point[aux] = int(posLivre)
					o+=1
					contagem+=1
				else:
					aux = point[aux]
					contagem+=1
			#Mudar o apontador para a próxima posição livre do arquivo		
		while (hashTable[posLivre] != "vazio"):
			posLivre -=1
			if(posLivre<0):
				print("arquivo cheio!")
				break
		qntInteiros +=1
	print("Tabela hashing após o processo:")
	print(hashTable)
	print("-----------------------------------------------------------------------")
	print("Tabela de apontadores após o processo:")
	print(point)
	print("-----------------------------------------------------------------------")
	print("Média de acessos: ")
	print(contagem/(len(inteiros)-1))




#-----------------------Função Principal---------------------------------
#Inserir o nome do .txt sem a extensão
print("Insira o nome do arquivo .txt que será utilizado para efetuar o Hashing: ")
nomeDoarquivo = input()
nomeDoarquivo = nomeDoarquivo + ".txt"

#Leitura do arquivo .txt
with open("Explícito com uso de ponteiros/" + nomeDoarquivo, "r") as arquivo:
	texto = arquivo.readlines()

#inicialização das listas e variavéis que serão utilizadas
inteiros = []
hashTable = []
point = []
cont = 0
contagem =0
#Criação de uma lista com os inteiros lidos do arquivo .txt
for i in texto:
	inteiros.append(int(i))

#Preenchimento da tabela Hashing e da tabela dos apontadores
while (cont<inteiros[0]):
	hashTable.append("vazio")
	point.append("vazio")
	cont +=1
	
insertion(hashTable, point, contagem)

with open("Explícito com uso de ponteiros/outputE.txt", "a") as arquivo:
	arquivo.write("--Tabela Hashing Encadeamento explÍcito com o uso de ponteiros usando alocação estática de memória --\n")
	
with open("Explícito com uso de ponteiros/outputE.txt", "a") as arquivo:
	arquivo.write("HashTable: \n" + str(hashTable))

with open("Explícito com uso de ponteiros/outputE.txt", "a") as arquivo:
	arquivo.write("\nApontadores: \n"+ str(point))
