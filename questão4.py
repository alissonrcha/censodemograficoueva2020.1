from censodemografico import lerarquivo

# ler arquivo
nomearquivo = 'censo.txt'
listapessoas = lerarquivo(nomearquivo)

# cabeçalho
print('-' * 15)
print('MÉDIA DE IDADES')
print('-' * 15)

# média de idade dos habitantes
somaidade = 0
for i in range(len(listapessoas)):
    idade = 2021 - listapessoas[i].anonascimento
    somaidade += idade
mediaidade = somaidade / len(listapessoas)
print(f'A média de idade dos habitantes é {mediaidade:.1f}')
