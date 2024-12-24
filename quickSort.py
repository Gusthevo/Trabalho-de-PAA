from randomArray import saveArray

def quick_sort(lista):
    if len(lista) <= 1:  # Caso base: listas de 0 ou 1 elemento já estão ordenadas
        return lista
    else:
        pivo = lista[-1]  # Pivô escolhido como o elemento do meio
        menor = [x for x in lista if x < pivo]  # Elementos menores que o pivô
        igual = [x for x in lista if x == pivo]  # Elementos iguais ao pivô
        maior = [x for x in lista if x > pivo]  # Elementos maiores que o pivô
        return quick_sort(menor) + igual + quick_sort(maior)


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

# Aplicando o Quick Sort
arrayOrdenado = quick_sort(arrayFromFile)
print("\nArray ordenado usando Quick Sort:", arrayOrdenado)
