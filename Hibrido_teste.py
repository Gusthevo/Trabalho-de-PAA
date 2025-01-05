from randomArray import saveArray

# Função para realizar o Insertion Sort em um subarray
# O objetivo é organizar os elementos no intervalo [left, right]
def insertion_sort(arr, left, right):
    # Percorre o subarray a partir do segundo elemento (índice left + 1)
    for i in range(left + 1, right + 1):
        key = arr[i]  # Armazena o elemento atual
        j = i - 1     # Começa a verificar elementos à esquerda
        # Move os elementos maiores que 'key' uma posição para frente
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # Insere o elemento 'key' na posição correta
        arr[j + 1] = key

# Função para realizar a operação de merge em dois subarrays ordenados
# Combina os subarrays arr[left:mid+1] e arr[mid+1:right+1] em um único array ordenado
def merge(arr, left, mid, right):
    # Calcula os tamanhos dos dois subarrays
    n1 = mid - left + 1  # Tamanho do subarray esquerdo
    n2 = right - mid     # Tamanho do subarray direito

    # Cria cópias dos subarrays
    L = arr[left:mid + 1]   # Subarray esquerdo
    R = arr[mid + 1:right + 1]  # Subarray direito

    # Inicializa os índices para percorrer os subarrays L, R e o array original
    i = j = 0  # Índices para L e R
    k = left   # Índice para o array original

    # Combina os elementos de L e R no array original arr
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]  # Insere o menor elemento de L
            i += 1
        else:
            arr[k] = R[j]  # Insere o menor elemento de R
            j += 1
        k += 1

    # Insere os elementos restantes de L (se houver)
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Insere os elementos restantes de R (se houver)
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# Função principal: Algoritmo híbrido que combina Merge Sort e Insertion Sort
def hybridMergeSort(arr, left, right, threshold=10):
    # Verifica se o array contém mais de um elemento
    if left < right:
        # Se o tamanho do subarray for menor que o limiar (threshold), usa Insertion Sort
        if right - left + 1 < threshold:
            insertion_sort(arr, left, right)
        else:
            # Caso contrário, aplica o Merge Sort
            mid = (left + right) // 2  # Calcula o índice do meio
            # Recursivamente ordena a metade esquerda
            hybridMergeSort(arr, left, mid, threshold)
            # Recursivamente ordena a metade direita
            hybridMergeSort(arr, mid + 1, right, threshold)
            # Mescla as duas metades ordenadas
            merge(arr, left, mid, right)



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

# Aplicando o Hybrid Sort
hybridMergeSort(arrayFromFile, 0, len(arrayFromFile) - 1)
print("\nArray ordenado usando  Hybrid Sort:", arrayFromFile)