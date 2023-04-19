
#-----------------------Função de Inserção-------------------------------
def insertion(hashTable):

#Variavés de controle
	qntInteiros = 1 
	aux=0
#inserção
	while(qntInteiros < len(inteiros)):
		aux = int(inteiros[qntInteiros]%inteiros[0])
		while (hashTable[aux] != "vazio"):
			aux+=1
			if aux == inteiros[0]:
				aux=-1
			
			elif aux == int(inteiros[qntInteiros]%inteiros[0]) :
				print("arquivo cheio!")
				qntInteiros = len(inteiros)
				break
			
		if(hashTable[aux] == "vazio"):
			hashTable[aux] = int(inteiros[qntInteiros])
			qntInteiros +=1	

#-----------------------Função Principal-------------------------------
#Inserir o nome do .txt sem a extensão
print("Insira o nome do arquivo .txt que será utilizado para efetuar o Hashing: ")
nomeDoarquivo = input()
nomeDoarquivo = nomeDoarquivo + ".txt"

#Leitura do arquivo .txt
with open("Trabalho1_EDA2/Explícito com uso de ponteiros/" + nomeDoarquivo, "r") as arquivo:
	texto = arquivo.readlines()

#inicialização das listas e variavéis que serão utilizadas
inteiros = []
hashTable = []
cont = 0

#Criação de uma lista com os inteiros lidos do arquivo .txt
for i in texto:
	inteiros.append(int(i))

#Preenchimento da tabela Hashing e da tabela dos apontadores
while (cont<inteiros[0]):
	hashTable.append("vazio")
	cont +=1
	
insertion(hashTable)

with open("Linear Probing/outputLP.txt", "a") as arquivo:
	arquivo.write("--Tabela Hashing utilizando Linear Probing --\n")

with open("Linear Probing/outputLP.txt", "a") as arquivo:
	arquivo.write("HashTable: \n" + str(hashTable))


print("Tabela hashing após o processo:")
print(hashTable)
