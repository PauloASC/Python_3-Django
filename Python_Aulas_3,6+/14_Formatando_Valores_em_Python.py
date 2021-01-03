"""
Formatando valores com modificadores

:s - Texto(strings)
:d - Inteiros(int/integer)
:f - Numeros de ponto flutuante(float)
:.{numero que vocÊ deseja ou precisa}f - Quantidade de decimais(float)
:{caractere}{> ou < ou ^}{quantidade}{tipo - s, d ou f}

> - Direita
< - Esquerda
^ - Centro
"""
# A operação a seguir vasi dar uma dizima periodica (não calcula para sempre mas 
# ainda sim mostra um resultado grande). 
num_1 = 10
num_2 = 3
divi = num_1 / num_2
print(divi)

# Para exibir menos numeros é possivel utilizar a função ajudante .format
# É possivel utiliza-la diretamente ou com auxilio da f string. No caso você esta
# definindo que quer utilizar uma formatação com dois pontos, com o ponto que você
# deseja formatar um numero depois da virgula ,coloca o numero de numeros apos a
# virgula a serem exibidos e por fim coloca f confirmando que é um float
print('{:.2f}'.format(divi))

# No caso da f string se faz de maneira parecida
print( f'{divi:.3f}')