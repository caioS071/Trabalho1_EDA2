from hashing import HashTable

hash_table = HashTable(11, "records.txt")

# Inserindo os registros
hash_table.insert(22, 2)
hash_table.insert(54, 7)
hash_table.insert(29, 5)
hash_table.insert(38, 9)
hash_table.insert(42, 8)

# Imprimindo a tabela de hashing
print("Índice\tValor")
for i, item in enumerate(hash_table.hash_table):
    print(f"{i}\t{item}")

# Procurando registros
print(f"Valor para a chave 22: {hash_table.search(22)}")
print(f"Valor para a chave 54: {hash_table.search(54)}")
print(f"Valor para a chave 29: {hash_table.search(29)}")
print(f"Valor para a chave 38: {hash_table.search(38)}")
print(f"Valor para a chave 42: {hash_table.search(42)}")
print(f"Valor para a chave 10: {hash_table.search(10)}")
