from censodemografico import lerarquivo, gravararquivo

# ler arquivo
nomearquivo = 'censo.txt'
listapessoas = lerarquivo(nomearquivo)

# cabeçalho
print('-' * 14)
print('INFORMAR ÓBITO')
print('-' * 14)

# informar óbito de pessoa
nome = input('Digite o nome da pessoa falecida: ')
indice = -1
for i in range(len(listapessoas)):
    if listapessoas[i].nome == nome:
        indice = i

if indice == -1:
    print('Pessoa não encontrada!')
else:
    del listapessoas[indice]
    print('Pessoa deletada do censo demogŕafico!')

# gravar arquivo
gravararquivo(nomearquivo, listapessoas)
