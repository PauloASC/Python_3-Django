# Cada caractere de uma string tem um indice, inclusive o espaço.
texto = 'Python S2'

# Podemos chamar um unico ou mais elementos utilizndo como base o indice da string. Lembrando
# que indice inicia em 0 e indices são posições. Para se fazer isso se diz a variavel que
# você quer trabalhar e entre colchetes o indice
print(texto[2])

# Também é possivel chamar um numero chamando ele por um indice negativo. Nesse caso o indice
# não começa em 0 ou 1 e sim pelo numero de contagem (que não considera 0) do total de 
# caracteres da string.
print(texto[-7])


# Alem de poder pegar uma unica letra, também é possivel pegar um trecho do texto ao utilizar
# o chamado fatiamento

# Nós podemos deteminar um inicio e um fim para o fatiamento. Porem lembre-se, o indice que
# marca o fim do fatiamento não aparece. Ou seja sempre some 1 quando você quiser buscar
# um trecho. E não se preocupe, nesse caso ele permite utilizar um indice que seja 1 numero 
# maior do que a quantidade de caracteres
print(texto[2:7])

# Para mandar o fatiamento pegar uma string do inicio ao fim, a maneira mais facil e 
# geralmente a mais correta é designar o inicio e deixar o fim vazio. Isso faz com que o
# fatiamento va até o final da string.
print(texto[2:])

# Outra maneira de se fazer fatiamento é definir um fim e deixar a esquerda vazia. Assim
# dizendo que é para começar do inicio
print(texto[:7])

# Uma coisa interessante que pode ser feita com o fatiamento incluindo numero negativo é
# excluir letras no final. 
file = 'oi.py'
print(file[:-3])

# Existe também a possibilidade de se utilizar um fatiamento que pule alguns caracteres.
# O numero da esquerda é o começo, o numero do meio é até aonde vai e o da direita é o
# numero de passo. Avisando que o passo sera feito com base em contagem. Como assim?
# O passo tem sua propria contagem e não usa posição ou indice. Quando você digita 2 por
#  exemplo ele pula a contagem 1 e mostra a contagem 2
print(texto[0::2])

# E sim pode se colocar um fim e ele sera respeitado ao utilizar o passo
print(texto[0:6:2])