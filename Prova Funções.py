
notas = []

def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media

def verificar_situacao(media):
    if media < 7:
        return 'Reprovado'
    elif media >= 7:
        return 'Aprovado'
    elif media == 10:
        return 'Parabens você tirou 10'

while True:
    nota = (input('Digite uma nota ou digite (fim) para sair: ')).strip().lower()

    if nota == 'fim':
        break
    try:
        nota = float(nota)
        notas.append(nota)
    except ValueError:
        print('digite uma nota valida')


media = calcular_media(notas)
situacao = verificar_situacao(media)

print('Media: ', media)
print('situação: ', situacao)