from censodemografico import lerarquivo

# ler arquivo
nomearquivo = 'censo.txt'
listapessoas = lerarquivo(nomearquivo)

# cabeçalho
print('-' * 14)
print('MÉDIA SALARIAL')
print('-' * 14)

# média salarial
somasalario = 0
for i in range(len(listapessoas)):
    somasalario += listapessoas[i].salario
media = somasalario / len(listapessoas)
print(f'A média de salários é R${media:.2f}')
