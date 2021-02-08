from censodemografico import Pessoa, gravararquivo, lerarquivo

# ler arquivo
nomearquivo = 'censo.txt'
listapessoas = lerarquivo(nomearquivo)

# cabeçalho
print('-' * 19)
print('CADASTRO DE PESSOAS')
print('-' * 19)

# cadastrar pessoa
pessoa = Pessoa()
pessoa.nome = input('Digite o nome da pessoa: ')
pessoa.estadocivil = input('Digite o estado civíl (C para casado e S para solteiro): ')
pessoa.anonascimento = int(input('Digite o ano de nascimento da pessoa: '))
pessoa.salario = float(input('Digite o salário da pessoa: '))
print('Pessoa cadastrada com êxito!')

# gravararuivo
listapessoas.append(pessoa)
gravararquivo(nomearquivo, listapessoas)
