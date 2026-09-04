### Para rodar o programa basta clicar no símbolo de play, ou SHIFT + F10 no teclado.

import random # importar a biblioteca para evitar repetir testes à mão

l = [i for i in range(0, 10001, 2)] # lista criada com números de 0 a 10000 de 2 em 2 (ou seja, terão apenas números pares na lista

def binary_search(lista, alvo):
    lista.sort() # garantir a ordenação da lista pro algoritmo funcionar
    left = 0 # definimos a extremidade esquerda como indice 0
    right = len(lista)-1 # definimos a extremidade direita como o último indice, que é o mesmo que o tamanho da lista - 1

    while left <= right: # enquanto a extremidade esquerda for menor ou igual à direita, o código continua verificando se tem o número na lista

        mid = (left + right)//2 # pegamos o indice do meio da lista somando as extremidades e dividindo inteiramente por 2
        num = lista[mid] # armazenamos o número que está na lista com o indice do meio

        if num == alvo: # condição para o momento que achar o número (se achar)
            return f'Número {alvo} encontrado na lista!'

        elif num < alvo: # condição para eliminar a metade esquerda se a tentativa/chute seja menor que o alvo
            left = mid+1

        else: # condição para eliminar a metade direita se a tentativa/chute seja maior que o alvo
            right = mid-1

    return f'Número não encontrado...' # retorna a string se cair nessa condição de não ser encontrado

numero_selecionado = random.randint(1, 10001) # seleciona um número para os casos de teste aleatoriamente entre 1 e 10001 (podendo retornar todos os caminhos do algoritmo)
print(f'Número alvo: {numero_selecionado}') # mostra qual é o número sorteado acima

print(binary_search(l, numero_selecionado)) # chama a função e coloca o código para rodar

### Código sobre busca binária bem básico para aprender o algoritmo
### Aprendido através do livro Entendendo Algoritmos - Um Guia Ilustrado Para Programadores e Outros Curiosos - Autor (Aditya Y. Bhargava)
### Tem como ocorrer vários erros, mas como mencionado acima, não é para ser algo muito foda, só aprendizado...