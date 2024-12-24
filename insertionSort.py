from randomArray import saveArray

# Função de Insertion Sort
def insertionSort(lista):
    tamanhoLista = len(lista)
    for j in range(1, tamanhoLista):
        chave = lista[j]
        i = j - 1    
        # Mover os elementos da lista que são maiores que a chave
        while i >= 0 and chave < lista[i]:
            lista[i + 1] = lista[i]
            i -= 1 
        # Aqui é inserida a chave na posição correta
        lista[i + 1] = chave
    # Aqui é retornada a lista ordenada
    return lista


# Ler e resgatar o array do arquivo
try:
    with open(saveArray, 'r') as k:
        content = k.read()
        # Convertendo a string de volta para uma lista
        arrayFromFile = eval(content)
        #print("\nArray resgatado do arquivo:", arrayFromFile)
except IOError as e:
    print(f"Erro ao ler o arquivo: {e}")
    arrayFromFile = []

# Aplicando o Insertion Sort
arrayOrdenado = insertionSort(arrayFromFile)
print("\nArray ordenado usando Insertion Sort:", arrayOrdenado)
