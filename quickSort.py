'''
Ordenação Rápida (Quicksort)
Ordenar listas.
Complexidade: O(n log n) na média.
'''


def quickSort(lista):
   quickSortHelper(lista,0,len(lista)-1)

def quickSortHelper(lista,primeiro,ultimo):
   if primeiro<ultimo:

       splitpoint = partition(lista,primeiro,ultimo)

       quickSortHelper(lista,primeiro,splitpoint-1)
       quickSortHelper(lista,splitpoint+1,ultimo)


def partition(lista,primeiro,ultimo):
   pivotvalue = lista[primeiro]

   leftmark = primeiro+1
   rightmark = ultimo

   done = False
   while not done:

       while leftmark <= rightmark and lista[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while lista[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = lista[leftmark]
           lista[leftmark] = lista[rightmark]
           lista[rightmark] = temp

   temp = lista[primeiro]
   lista[primeiro] = lista[rightmark]
   lista[rightmark] = temp


   return rightmark

lista = [54,26,93,17,77,31,44,55,20]
print("Lista desordenada: ")
print(lista)
quickSort(lista)
print("Lista ordenada: ")
print(lista)