import random

num_amostras = 40
tam_tabela = 50
fator_de_carga = num_amostras/tam_tabela
count = 0
while count < 10:
    file_name = f'test{count}_fator_ {fator_de_carga}.txt'
    with open(file_name, 'w') as f:
        f.write(str(num_amostras) + '\n')
        for num in range(num_amostras):
            f.write(str(random.randint(1, 50)) + '\n')
    count += 1