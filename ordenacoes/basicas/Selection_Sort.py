### SHIFT+F10 to run
import random # evitar fazer casos de teste a mão...

array = []
for x in range(10):
    num = random.randint(1, 10)
    array.append(num)
# array contendo números aleatórios de 1 a 10, para casos de teste.

print(f"Lista não ordenada -> {array}")

def selection_sort(lista):
    tamanho_lista = len(lista) # pegamos o tamanho da lista em um inteiro

    for i in range(tamanho_lista - 1): # um for percorrendo todos os itens da lista
        indice_menor = i # definimos o indice menor sendo o indice atual no momento

        for j in range(i + 1, tamanho_lista): # pega o proximo item da lista (j)
            if lista[j] < lista[indice_menor]: # compara o indice "j" com o anterior
                indice_menor = j # altera o valor de indice_menor para "j" se a condição for True

        if indice_menor != i: # se indice_menor tiver um valor diferente de "i" troca o valor "i" com "indice_menor"
            lista[i], lista[indice_menor] = lista[indice_menor], lista[i]

    return f"Lista ordenada com Selection Sort -> {lista}" # retorno da lista ordenada

print(selection_sort(array)) # chamada da função