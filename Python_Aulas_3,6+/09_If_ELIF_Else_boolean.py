"""
Condições IF, Elif e Else
"""
# If, Else e Elif são verificadores que se baseiam em boolean (TRUE ou FALSE) para determinar
# o que deve ser feito. Se uma ação deve ser feita caso seja verdadeiro ou outra caso seja 
# falso. No caso o If é a primeira linha de verificação. Não se começa por else ou elif
# Nunca esquecer de colocar o que você deseja verificar com if em uma identação (Tab ou 4
# barras de espaço).
# O if pode verificar qualquer coisa. E não precisa de else para funcionar, mas é bom ter
# O if só sera executado caso seja true o resultado. Caso seja False o if sera completamente
 #ignorado e o código rodara normalmente. Mas existe uma maneira de continuar caso seja falso
if False:
    print('Verdadeiro')
# O else é uma ação que pode ocorrer caso o if de resultado false. Porem ele só pode ser 
# utilizado uma vez por condição. 
else:
    print('Código rodando')


if False:
    print('Verdadeiro')

# Para resolver o problema de não poder utilizar mais de um else, existe o elif, que pode ser
# utilizado varias vezes.
elif True:
    print('Elif')

else:
    print('Código rodando')