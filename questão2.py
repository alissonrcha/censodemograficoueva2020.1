from censodemografico import lerarquivo, gravararquivo

# ler arquivo
nomearquivo = 'censo.txt'
listapessoas = lerarquivo(nomearquivo)

# cabeçalho
print('-' * 13)
print('ALTERAR DADOS')
print('-' * 13)

# alterar dados
nome = input('Digite o nome da pessoa para alterar os dados: ')
for i in range(len(listapessoas)):
    if listapessoas[i].nome == nome:
        print('Pessoa encontrada!')
        listapessoas[i].nome = input('Digite o nome da pessoa: ')
        listapessoas[i].estadocivil = input('Digite o estado civíl (C para casado e S para solteiro): ')
        listapessoas[i].anonascimento = int(input('Digite o ano de nascimento: '))
        listapessoas[i].salario = float(input('Digite o salário da pessoa: '))
        print('Dados alterados com êxito!')

# gravararquivo
gravararquivo(nomearquivo, listapessoas)
