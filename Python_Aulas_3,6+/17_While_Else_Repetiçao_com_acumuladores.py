contador = 0

while contador < 100:
    print(contador)
    contador += 1


# Alem dos contadores existem os acumuladores. Eles litealmente acumulam um valor e o 
# incrementam só mais tarde
acumulador = 1
contador = 1

while contador <= 10:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador += 1

# Diferente de varias linguagens de programação. O Python permite o uso de else dentro do
# while, sem a necessidade do if.
acumulador = 1
contador = 1

while contador <= 10:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador += 1
else:
    print('Fim da contagem')