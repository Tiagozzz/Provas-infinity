lista_numeros = []
lista_pares = []
lista_impares = []

for i in range (1,11):
    numero = int(input('Digite o numero:'))

    lista_numeros.append(numero)

    if numero % 2 == 0:
        lista_pares.append(numero)
    elif numero % 2 == 1:
        lista_impares.append(numero)
        
print('Numeros pares: ', tuple(lista_pares))
print('Numeros impares: ', tuple(lista_impares))

print('Quantidade de numeros pares: ', (len(lista_pares)))
print('Quantidade de numeros impares: ', (len(lista_impares)))

soma_pares = sum(lista_pares)
soma_impares = sum(lista_impares)

print('Soma dos numeros pares: ', soma_pares) 
print('Soma dos numeros impares: ', soma_impares) 