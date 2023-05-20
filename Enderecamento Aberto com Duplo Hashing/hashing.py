import math

print("Insira o nome do arquivo .txt que será utilizado para efetuar o Hashing: ")
nomeDoarquivo = input()
nomeDoarquivo = nomeDoarquivo + ".txt"

chaves = []
hashTable = []

with open("Enderecamento Aberto com Duplo Hashing/" + nomeDoarquivo, "r") as arquivo:
	entrada = list(map(int,arquivo.readlines()))
	
capacidadeArquivo = entrada[0]
for i in range(1,len(entrada)):
	chaves.append(entrada[i])

for i in range(capacidadeArquivo):
	hashTable.append("vazio")

def funcaoHash1(chave):
	return chave % capacidadeArquivo

def funcaoHash2(chave):
	if chave >= capacidadeArquivo:
		return math.floor(chave/capacidadeArquivo)
	else:
		return 1

def insertion(hashTable, chaves):
    posLivre = capacidadeArquivo 
    numeroDeAcessos = 0

    for i in chaves:
        if(posLivre == 0):  
            print("arquivo cheio!")
            break

        hash1 = funcaoHash1(i)
        hash2 = funcaoHash2(i)

        if(hashTable[hash1] == "vazio"):
            hashTable[hash1] = i
            numeroDeAcessos += 1
            # print(numeroDeAcessos, i, hash1)
        else:
            impossivel = 0
            while(hashTable[hash1] != "vazio"):
                numeroDeAcessos += 1
                # print(numeroDeAcessos, i, hash1)
                if hash2 >= capacidadeArquivo:
                    hash2 = funcaoHash1(hash2)
                hash1 += hash2
                if(hash1 >= capacidadeArquivo):
                    hash1 = funcaoHash1(hash1)  
                impossivel += 1
                if(impossivel == capacidadeArquivo):
                    print("É impossível inserir o registro:", i)
                    numeroDeAcessos -= 1
                    break
            numeroDeAcessos += 1
            # print(numeroDeAcessos, i, hash1)         
            hashTable[hash1] = i
    
        posLivre -= 1
        print(numeroDeAcessos )
        # print(hashTable)
	
    return numeroDeAcessos

numeroDeAcessos = insertion(hashTable, chaves)

with open("Enderecamento Aberto com Duplo Hashing/outputDH.txt", "a") as arquivo:
	arquivo.write("--Tabela Enderecamento aberto com Duplo Hashing --\n")
	
with open("Enderecamento Aberto com Duplo Hashing/outputDH.txt", "a") as arquivo:
	arquivo.write("HashTable: \n" + str(hashTable))

print("Tabela hashing após o processo:")
print(hashTable)
print("Media de acessos: " + str(numeroDeAcessos/len(chaves)))
# print(numeroDeAcessos)
# print(len(chaves))