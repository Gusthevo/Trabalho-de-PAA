import random 
import os

# Função para gerar o tamanho do array e depois estamos declarando um array vazio
arraySize = 9999
arrayNotRepeated = []

arraysNotSorted = "arraysNotSorted"
# Cria o diretório para salvar o arquivo com o array
if not os.path.exists(arraysNotSorted):
    os.makedirs(arraysNotSorted)

#Gera o array aleatório que não se repete
arrayNotRepeated = random.sample(range(100000000), arraySize)
#print (arrayNotRepeated)
"""


#aqui seria um array que se repete
for i in range(arraySize):
    arrayExitCanBeRepeated.append(random.randint(0, 10))
print (arrayExitCanBeRepeated)
"""
#Sempre que for chamado, vai alterar a lista não ordenada para outra nova, já que chama saveArray, e write uma nova lista gerada
saveArray = os.path.join(arraysNotSorted, "array.txt")
# Verifica se a pasta existe e tentar salvar o arquivo
if os.path.exists(arraysNotSorted):
    try:
        with open(saveArray, 'w') as k:
            k.write(str(arrayNotRepeated))
            #print(f"Lista salva em: {arraysNotSorted}")
        with open(saveArray, 'r') as k:
            content = k.read()
            #print(content)
    except IOError:
        print(f"Erro ao salvar o array na pasta, veja o que tem de errado, meu rei{IOError}")