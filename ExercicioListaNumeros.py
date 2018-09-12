maior = menor = 1
lista = []
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
i = ini

for i in range(ini,fim+1):
    i+=0
    lista.append(i)
print(lista)
print('Maior: {}'.format(max(lista)))
print('Menor: {}'.format(min(lista)))