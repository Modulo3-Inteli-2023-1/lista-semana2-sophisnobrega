# definindo a função 
def conta_palavras_unicas(frase: str) -> int: # entra string e sai inteiro
    return len(set(frase.split())) # retorna o tamanho da lista que se deu pelo slip da frase a cada espaço

# -------------- OPÇÃO DE OUTPUT ------------------ #
#frase = input('Escreva uma frase ou um parágrafo: ')
#quantidade = conta_palavras_unicas(frase)
#print('Quantidade de palavras únicas:', quantidade)







