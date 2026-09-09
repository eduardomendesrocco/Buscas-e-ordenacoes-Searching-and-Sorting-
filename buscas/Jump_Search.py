import random, math

array = [i for i in range(1, 10001, 2)]

def jump_search(lista, alvo):
    tamanho_lista = len(lista)
    jump = int(math.sqrt(tamanho_lista))

    inicio, fim = 0, 0
    while fim < tamanho_lista and lista[fim] < alvo:
        inicio = fim
        fim += jump

    fim = min(fim, tamanho_lista - 1)

    for numero in range(inicio, fim + 1):
        if lista[numero] == alvo:
            return f"Número {alvo} encontrado!" # encontrado

    return "Não encontrado"

numero_selecionado = random.randint(1, 10000)

print(f"Número alvo -> {numero_selecionado}")
print(jump_search(array, numero_selecionado))