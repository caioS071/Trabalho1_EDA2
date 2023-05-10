
#-----------------------Função de Inserção-------------------------------
def insertion(hashTable, contagem):

#Variavés de controle
	qntInteiros = 1 
	aux=0
#inserção
	while(qntInteiros < len(inteiros)):
		aux = int(inteiros[qntInteiros]%inteiros[0])
		while (hashTable[aux] != "vazio"):
			aux+=1

			if aux == int(inteiros[qntInteiros]%inteiros[0]) :
				print("arquivo cheio!")
				qntInteiros = len(inteiros)
				break

			contagem+=1
			if aux == inteiros[0]:
				aux=0			
			
		if(hashTable[aux] == "vazio"):
			hashTable[aux] = int(inteiros[qntInteiros])
			contagem+=1
			qntInteiros +=1	
	
	print("Tabela hashing após o processo:")
	print(hashTable)
	print("-----------------------------------------------------------------------")
	print(contagem)
	print("Média de acessos: ")
	print(contagem/(len(inteiros)-1))




#-----------------------Função Principal-------------------------------
#Inserir o nome do .txt sem a extensão
print("Insira o nome do arquivo .txt que será utilizado para efetuar o Hashing: ")
nomeDoarquivo = input()
nomeDoarquivo = nomeDoarquivo + ".txt"

#Leitura do arquivo .txt
with open("Linear Probing/" + nomeDoarquivo, "r") as arquivo:
	texto = arquivo.readlines()

#inicialização das listas e variavéis que serão utilizadas
inteiros = []
hashTable = []
cont = 0
contagem = 0

#Criação de uma lista com os inteiros lidos do arquivo .txt
for i in texto:
	inteiros.append(int(i))

#Preenchimento da tabela Hashing e da tabela dos apontadores
while (cont<inteiros[0]):
	hashTable.append("vazio")
	cont +=1
	
insertion(hashTable, contagem)

with open("Linear Probing/outputLP.txt", "a") as arquivo:
	arquivo.write("\n--Tabela Hashing utilizando Linear Probing --\n")

with open("Linear Probing/outputLP.txt", "a") as arquivo:
	arquivo.write("HashTable: \n" + str(hashTable))

