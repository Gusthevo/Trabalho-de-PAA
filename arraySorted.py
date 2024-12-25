import os

# Função para gerar o tamanho do array e depois estamos declarando um array vazio
arraySize = 99999
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
def bubbleSort(lista):
    tamanhoLista = len(lista)
    for i in range(tamanhoLista):
        swapped = False 
        for j in range(0, tamanhoLista-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                swapped = True
        if not swapped:
            break

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

# Aplicando o Bubble Sort
bubbleSort(arrayFromFile)
print("\nArray ordenado usando Bubble Sort:", arrayFromFile)
