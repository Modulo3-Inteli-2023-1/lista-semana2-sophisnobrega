# função que faz a separação das letras e coloca em uma lista
def letras_da_palavra(palavra: str) -> list:
    letras = list(palavra)
    return letras

# input das palavras
palavra_a = input('Escreva uma palavra: ')
palavra_b = input('Escreva outra palavra: ')

# função principal que confere se é anagrama ou não
def is_anagram(palavra_a, palavra_b):
    letras_a = letras_da_palavra(palavra_a)
    letras_b = letras_da_palavra(palavra_b)
    
    letras_a.sort()  # ordena as letras
    letras_b.sort()  
    
    return letras_a == letras_b

e_anagrama = is_anagram(palavra_a, palavra_b)
print(e_anagrama)

# usei o chat gpt para me ajudar a corrijir o código
# no vs code está funcionando tranquilamente












