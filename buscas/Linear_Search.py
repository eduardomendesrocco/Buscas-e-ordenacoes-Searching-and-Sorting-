### SHIFT+F10 to run
import random # importei a biblioteca random para evitar digitar casos de teste a mão

array = [i for i in range(1, 10001, 2)] # cria uma lista com os números de 1 a 10000 a cada dois
### nesse caso em específico do meu código o array contém apenas números ímpares...
### se trocássemos a definição do array para --> [i for i in range(0, 10001, 2)]
### o array seria definido apenas com pares, pois começaria no 0 e não no 1 como feito.

def linear_search(lista, alvo):

    for number in lista: # um for para percorrer a lista toda

        if number == alvo: # condição para achar o número alvo
            return f"Número encontrado!" # return se achar

    return f"{alvo} não foi encontrado na lista..." # return se não achar

numero_selecionado = random.randint(1, 10000) # número aleatório de 1 a 10000 para ser o alvo

print(f"Número alvo -> {numero_selecionado}") # print do número aleatório alvo
print(linear_search(array, numero_selecionado)) # chamar a função

