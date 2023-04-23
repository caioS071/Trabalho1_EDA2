import math
capacidadeArquivo = 11 

def funcaoHash1(chave):
	return chave % capacidadeArquivo

def funcaoHash2(chave):
	if chave >= capacidadeArquivo:
		return math.floor(chave/capacidadeArquivo)
	else:
		return 1

def insertion(hashTable, chaves):
    posLivre = capacidadeArquivo 
	
    for i in chaves:
        if(posLivre == 0):  
            print("arquivo cheio!")
            break

        hash1 = funcaoHash1(i)
        hash2 = funcaoHash2(i)

        if(hashTable[hash1] == "vazio"):
            hashTable[hash1] = i
        else:
            while(hashTable[hash1] != "vazio"):
                hash1 += hash2
                if hash1 >= capacidadeArquivo:
                    hash1 = hash1 - capacidadeArquivo
            hashTable[hash1] = i
	    
        posLivre -= 1

print("Insira o nome do arquivo .txt que será utilizado para efetuar o Hashing: ")
nomeDoarquivo = input()
nomeDoarquivo = nomeDoarquivo + ".txt"

chaves = []
hashTable = []

with open("Enderecamento Aberto com Duplo Hashing/" + nomeDoarquivo, "r") as arquivo:
	chaves = map(int,arquivo.readlines())
	
for i in range(capacidadeArquivo):
	hashTable.append("vazio")

insertion(hashTable, chaves)

with open("Enderecamento Aberto com Duplo Hashing/outputDH.txt", "a") as arquivo:
	arquivo.write("--Tabela Enderecamento aberto com Duplo Hashing --\n")
	
with open("Enderecamento Aberto com Duplo Hashing/outputDH.txt", "a") as arquivo:
	arquivo.write("HashTable: \n" + str(hashTable))

print("Tabela hashing após o processo:")
print(hashTable)