import os

# Função para gerar o tamanho do array e depois estamos declarando um array vazio
arraySize = 1100
arraySorted = list(range(arraySize))  # Gera um array ordenado de 0 a arraySize-1

arraysSorted = "arraysSorted"
# Crição do diretório para salvar o arquivo com o array
if not os.path.exists(arraysSorted):
    os.makedirs(arraysSorted)

# Salva o array ordenado em um arquivo
saveArraySorted = os.path.join(arraysSorted, "arraysSorted.txt")
try:
    with open(saveArraySorted, 'w') as k:
        k.write(str(arraySorted))  # Salva o array como uma string
        # print(f"Lista ordenada salva em: {saveArraySorted}")
except IOError as e:
    print(f"Erro ao salvar o array: {e}")

"""
# Função de partição para o QuickSort
def partition(array, start, end):
    pivo = array[end]  # Pivô é o último elemento
    smaller_index = start - 1  # Índice do menor elemento
    for current_index in range(start, end):
        if array[current_index] <= pivo:
            smaller_index += 1
            array[smaller_index], array[current_index] = array[current_index], array[smaller_index]  # Troca elementos menores ou iguais ao pivô
    array[smaller_index + 1], array[end] = array[end], array[smaller_index + 1]  # Coloca o pivô na posição correta
    return smaller_index + 1

# Função de QuickSort
def quickSort(array, start, end):
    if start < end:
        partition_index = partition(array, start, end)  # Índice da partição
        quickSort(array, start, partition_index - 1)  # Recursivamente ordena os elementos antes da partição
        quickSort(array, partition_index + 1, end)  # Recursivamente ordena os elementos depois da partição
"""
"""
#Implementação do Bubble Sort
def bubbleSort(lista):
    tamanhoLista = len(lista)
    for i in range(tamanhoLista): 
        for j in range(0, tamanhoLista-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
"""
"""
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
"""

"""
def mergeSort(lista):
    #Caso base quando a lista tem tamanho 1, significa que está ordenada
    if len(lista) <= 1:
        return lista
    #Faz divisões por dois, dividindo em lado esquerdo e direito
    metadeLista = len(lista) // 2
    # Atribui a metade da esquerda para um e a da direita para outra metade
    leftHalf = lista[:metadeLista]
    rightHalf = lista[metadeLista:]

    #Recursivamente ordena os dois lados
    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)

# Função para mergear dois arrays ordenados
def merge(left, right):
    #Declara um array vazio
    array = []
    i = j = 0
    #Laço de repetição para ser executado enquanto o valor de i e j forem menores que a esquerda e direita
    while i < len(left) and j < len(right):
        # Se o valor da esquerda for menor ou igual ao da direita, adiciona-o ao resultado e avança para a próxima posição
        if left[i] < right[j]:
            array.append(left[i])
            i += 1
            # Senão, adiciona-o ao resultado e avança para a próxima posição da direita
        else:
            array.append(right[j])
            j += 1
    # Por fim, adiciona todos os elementos restantes na lista
    array.extend(left[i:])
    array.extend(right[j:])

    return array
"""

# Aqui a gente abre o arquivo do array para depois aplicar algum dos algoritmos
try:
    with open(saveArraySorted, 'r') as k:
        content = k.read()
        arrayFromFile = eval(content)  # Converte a string de volta para uma lista
except IOError as e:
    print(f"Erro ao ler o arquivo: {e}")
    arrayFromFile = []
except Exception as e:
    print(f"Erro ao processar o conteúdo do arquivo: {e}")
    arrayFromFile = []

# Aplicando o Algoritmo
if arrayFromFile:
    #quickSort(arrayFromFile, 0, len(arrayFromFile) - 1)
    print("\nArray ordenado usando QuickSort:", arrayFromFile)  
else:
    print("Erro: Não foi possível carregar o array. Encerrando...")
