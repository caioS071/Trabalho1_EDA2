
#-----------------------Função de Inserção-------------------------------
#def insertion(hashTable, point):

#Variavés de controle
	
#inserção
	

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
	

#insertion(hashTable, point)

with open("Trabalho1_EDA2/Linear Probing/outputLP.txt", "a") as arquivo:
	arquivo.write("HashTable: \n" + str(hashTable))

with open("Trabalho1_EDA2/Linear Probing/outputLP.txt", "a") as arquivo:
	arquivo.write("\nApontadores: \n"+ str(point))


print("Tabela hashing após o processo:")
print(hashTable)
print("-----------------------------------------------------------------------")
print("Tabela de apontadores após o processo:")
print(point)