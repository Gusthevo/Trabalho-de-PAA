from randomArray import saveArray

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

# Ler e resgatar o array do arquivo
try:
    with open(saveArray, 'r') as k:
        content = k.read()
        # Convertendo a string de volta para uma lista
        arrayFromFile = eval(content)
       # print("\nArray resgatado do arquivo:", arrayFromFile)
except IOError as e:
    print(f"Erro ao ler o arquivo: {e}")
    arrayFromFile = []

# Aplicando o Merge Sort
arrayOrdenado = mergeSort(arrayFromFile)
print("\nArray ordenado usando Merge Sort:", arrayOrdenado)