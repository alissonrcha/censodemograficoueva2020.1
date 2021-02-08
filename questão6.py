from censodemografico import lerarquivo

# ler arquivo
nomearquivo = 'censo.txt'
listapessoas = lerarquivo(nomearquivo)

# cabeçalho
print('-' * 29)
print('PERCENTUAL DE PESSOAS CASADAS')
print('-' * 29)

# percentual de pessoas casadas
somacasados = 0
for i in range(len(listapessoas)):
    if listapessoas[i].estadocivil == 'C' or listapessoas[i].estadocivil == 'c':
        somacasados += 1
percentual = (somacasados / len(listapessoas)) * 100
print(f'O percentual de pessoas casadas é {percentual:.1f}%')
