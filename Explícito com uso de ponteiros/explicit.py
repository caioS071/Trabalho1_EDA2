#Inserir o nome do .txt sem a extensão
print("Insira o nome do arquivo .txt que será utilizado para efetuar o Hashing: ")
nomeDoarquivo = input()
nomeDoarquivo = nomeDoarquivo + ".txt"

#Leitura do arquivo .txt
with open(nomeDoarquivo, "r") as arquivo:
	texto = arquivo.readlines()

#inicialização das listas e variavéis que serão utilizadas
inteiros = []
hashTable = []
point = []
cont = 0

#Criação de uma lista com os inteiros lidos do arquivo .txt
for i in texto:
	inteiros.append(int(i))

#Preenchimento da tabela Hashing e da tabela dos apontadores
while (cont<inteiros[0]):
	hashTable.append("vazio")
	point.append("vazio")
	cont +=1
	
#Variavés de controle
posLivre = len(hashTable)-1
qntInteiros = 1  
aux=0
j=0

#inserção
while(qntInteiros < len(inteiros)):
	o=0
	aux = int(inteiros[qntInteiros]%inteiros[0])

	if hashTable[aux] == "vazio":
			hashTable[aux] = int(inteiros[qntInteiros])

	elif posLivre != -1:
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

	else:
		print("arquivo cheio!")

	qntInteiros +=1
print("Tabela hashing após o processo:")
print(hashTable)
print("-----------------------------------------------------------------------")
print("Tabela de apontadores após o processo:")
print(point)