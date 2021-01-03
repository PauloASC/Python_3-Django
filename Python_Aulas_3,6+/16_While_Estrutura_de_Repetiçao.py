# No Python é possivel criar loops de repetição. Um deles é o loop While. Que é executado
# enquanto a condição for true.
# Cuidado com loops infinitos. Se você criar um loop infinito não se assuste. De ctrl+c no
# terminal e isso ira encerrar a execução do código
#while True:
#    nome: input('Digite seu nome')

# Podemos criar condiçoes que podem sozinhas interromper um loop. Por exemplo criando um 
# contador que conte até 100. Ele inicia em 0 e o loop faz com que ele va aumentando de 1 em 1
x = 0
while x <= 100:
    print(x)
    x = x + 1

# O Python ira executar o código em ordem. Por isso mesmo que demore ou esteja em loop 
# infinito, a linguagem ira aguardar o fim do loop para continuar
print('Contagem realizada com sucesso!')

# Existe o comando continue. Ele consegue pular loops. Porem ele não pode ser usado sozinho
# senão não vai dar resultado nenhum. E diferente do pass ele não permite que o código
# prossiga após saber de sua existencia. Ele pode ser utilizado junto a um if desta maneira
x = 0
while x <= 10:
    if x ==3:
        x = x + 1
        continue
    print(x)
    x = x + 1

# Uma maneira de parar um loop é utilizar break. Ao realizar determinada ação ele para e sai
# do loop
x = 0
while x <= 10:
    if x ==3:
        x = x + 1
        break
    print(x)
    x = x + 1


# Da para colocar um while dentro de um outro while.
x = 0
while x < 10:
    y = 0
    while y < 5:
        print(f'X vale {x} e Y vale {y}.')
        y += 1
    
# Existe outra maneira de se somar algo a uma variavel, utilizando +=, assim poupando o
# uso de alguns caracteres
    x += 1