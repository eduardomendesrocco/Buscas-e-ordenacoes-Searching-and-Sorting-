### SHIFT+F10 to run
import random

array = []
for x in range(10):
    num = random.randint(1, 10)
    array.append(num)
# array contendo números aleatórios de 1 a 10, para casos de teste.

print(f"Lista não ordenada -> {array}")

def insertion_sort(lista):
    tamanho_lista = len(lista)

    for i in range(1, tamanho_lista):
        chave = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = chave

    return lista

print(f"Lista ordenada: {insertion_sort(array)}")