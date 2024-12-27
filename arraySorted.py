import os

# Função para gerar o tamanho do array e depois estamos declarando um array vazio
arraySize = 1000000
arraySorted = list(range(arraySize))  # Gera um array ordenado de 0 a arraySize-1

arraysSorted = "arraysSorted"
# Cria o diretório para salvar o arquivo com o array
if not os.path.exists(arraysSorted):
    os.makedirs(arraysSorted)

# Salva o array ordenado em um arquivo
saveArraySorted = os.path.join(arraysSorted, "arraysSorted.txt")
# Verifica se a pasta existe e tenta salvar o arquivo
if os.path.exists(arraysSorted):
    try:
        with open(saveArraySorted, 'w') as k:
            k.write(str(arraySorted))
            #print(f"Lista ordenada salva em: {saveArraySorted}")
    except IOError as e:
        print(f"Erro ao salvar o array: {e}")

#Implementação do Bubble Sort
def partition(array, start, end):
    middle = (start + end) // 2  # Pivô escolhido como o elemento do meio
    pivo = array[middle]
    array[middle], array[end] = array[end], array[middle]  # Move o pivô para o final para facilitar a partição
    smaller_index = start - 1  # Índice do menor elemento
    for current_index in range(start, end):
        if array[current_index] <= pivo:
            smaller_index += 1
            array[smaller_index], array[current_index] = array[current_index], array[smaller_index]  # Troca elementos menores ou iguais ao pivô
    array[smaller_index + 1], array[end] = array[end], array[smaller_index + 1]  # Coloca o pivô na posição correta
    return smaller_index + 1

def quickSort(array, start, end):
    if start < end:
        partition_index = partition(array, start, end)  # Índice da partição
        quickSort(array, start, partition_index - 1)  # Recursivamente ordena os elementos antes da partição
        quickSort(array, partition_index + 1, end)  # Recursivamente ordena os elementos depois da partição
# Aqui a gente abre o arquivo do array para depois aplicar o bubble nele
try:
    with open(saveArraySorted, 'r') as k:
        content = k.read()
        # Convertendo a string de volta para uma lista
        arrayFromFile = eval(content)
       # print("\nArray resgatado do arquivo:", arrayFromFile)
except IOError as e:
    print(f"Erro ao ler o arquivo: {e}")
    arrayFromFile = []

# Aplicando o Quick Sort
if arrayFromFile:
    quickSort(arrayFromFile, 0, len(arrayFromFile) - 1)
    print("\nArray ordenado usando Quick Sort:", arrayFromFile)
else:
    print("Erro: Não tem uma lista ou não foi carregado, meu rei. Encerrando...")
