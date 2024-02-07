'''
Busca Binária
Encontrar um elemento em uma lista ordenada.
Complexidade: O(log n).
'''

def busca_binaria(lista, elemento):

    ponteiro_inferior = 0
    ponteiro_superior = len(lista) - 1

    while ponteiro_inferior <= ponteiro_superior:
        ponteiro_meio = (ponteiro_inferior + ponteiro_superior) // 2

        if lista[ponteiro_meio] == elemento:
            return print("Elemento encontrado na posição", ponteiro_meio)
        elif lista[ponteiro_meio] < elemento:
            ponteiro_inferior = ponteiro_meio + 1
        else:
            ponteiro_superior = ponteiro_meio - 1
    
    return print("Elemento não encontrado")

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
busca_binaria(lista, int(input("Digite o número a ser buscado: ")))
