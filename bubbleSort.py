from randomArray import saveArray

#Implementação do Bubble Sort
def bubbleSort(lista):
    tamanhoLista = len(lista)
    for i in range(tamanhoLista): 
        for j in range(0, tamanhoLista-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

# Aqui a gente abre o arquivo do array para depois aplicar o bubble nele
try:
    with open(saveArray, 'r') as k:
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