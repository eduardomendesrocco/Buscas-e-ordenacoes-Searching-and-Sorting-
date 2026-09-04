### SHIFT+F10 to run
import random # evitar fazer casos de teste a mão...

array = [random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10)]
# array contendo números aleatórios de 1 a 10, para teste.

print(f"Lista não ordenada -> {array}")

def bubble_sort(lista):
    tamanho_lista = len(lista) # pegando o tamanho da lista

    for indice in range(tamanho_lista - 1): # o for externo controla quantas passagens serão feitas
        for j in range(tamanho_lista - 1 - indice): # o for interno vai comparar os elementos

            if lista[j] > lista[j + 1]: # compara o indice "j" da lista com o próximo

                lista[j], lista[j + 1] = lista[j + 1], lista[j] # altera os números para a ordenação

    return f"Lista ordenada com Bubble Sort -> {lista}" # retorno da lista ordenada

print(bubble_sort(array)) # chamada da função