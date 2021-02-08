class Pessoa:
    nome: str
    estadocivil: str
    anonascimento: int
    salario: float


# sub-rotina para ler arquivo
def lerarquivo(nomearquivo: str) -> list:
    listapessoas = []
    arquivo = open(nomearquivo, 'r')
    for linha in arquivo.readlines():
        lista = linha.split(',')
        pessoa = Pessoa()
        pessoa.nome = lista[0]
        pessoa.estadocivil = lista[1]
        pessoa.anonascimento = int(lista[2])
        pessoa.salario = float(lista[3])
        listapessoas.append(pessoa)
    return listapessoas


# sub-rotina para gravar arquivo
def gravararquivo(nomearquivo: str, listapessoas: list) -> None:
    arquivo = open(nomearquivo, 'w')
    for i in range(len(listapessoas)):
        arquivo.write(f'{listapessoas[i].nome},{listapessoas[i].estadocivil},'
                      f'{listapessoas[i].anonascimento},'
                      f'{listapessoas[i].salario}\n')
    arquivo.close()
