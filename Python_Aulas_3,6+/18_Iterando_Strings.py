# Iterar passar sobre cada elemento com indice
frase = "O rato roeu a roupa do rei de roma"
tamanho_frase = len(frase)
contador = 0


while contador < tamanho_frase:
    print(frase[contador], contador)
    contador += 1
