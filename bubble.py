''' 
Ordenação por Bolha, Inserção e Seleção
Métodos simples de ordenação.
O(n^2) na média e no pior caso. 
'''

def bubbleSort(lista):
    for passnum in range(len(lista)-1,0,-1):
        for i in range(passnum):
            if lista[i]>lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
lista = [54,26,93,17,77,31,44,55,20]
print("Lista embaralhada: ")
print(lista)
bubbleSort(lista)
print("Lista ordenada: ")
print(lista)