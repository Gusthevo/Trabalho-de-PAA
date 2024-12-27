import time
from mergeSort import mergeSort
import seaborn as sns
import matplotlib.pyplot as plt

# Caminho do arquivo
caminho_arquivo = "../TRABALHO 1/arraysNotSorted/array.txt"

try:
    # Tenta ler o conteúdo do arquivo
    with open(caminho_arquivo, 'r') as f:
        content = f.read()
        lista = eval(content)  # Convertendo a string de volta para uma lista
except IOError as e:
    print(f"Erro ao ler o arquivo: {e}")
    lista = []  # Define uma lista vazia em caso de erro

# Verifica se a lista foi carregada corretamente
if not lista:
    print("Erro: Não tem uma lista ou não foi carregado, meu rei. Encerrando...")
else:
    # Quantidade de execuções
    num_execucoes = 10

    # Lista para armazenar os tempos de execução
    tempos_merge_sort = []

    # Executar o Merge Sort várias vezes
    for i in range(num_execucoes):
        lista_copia = lista.copy()  # Cria uma cópia da lista original para cada execução
        print("Iniciando medição")
        startTime = time.perf_counter()  # Início da medição do tempo
        mergeSort(lista_copia)  # Executar o Merge Sort
        endTime = time.perf_counter()  # Fim da medição do tempo
        print("Acabou a medição")

        # Armazenar o tempo de execução em milissegundos
        tempo_execucao = (endTime - startTime) * 1000
        tempos_merge_sort.append(tempo_execucao)
        #print("\nLista ordenada :", lista_copia)


    # Exibir a lista ordenada da última execução
   # print("\nLista ordenada da última execução:", lista_copia)
    
    # Calcular o tempo médio
    tempo_medio_merge_sort = sum(tempos_merge_sort) / num_execucoes
    print(f"\nTempo médio do Merge Sort: {tempo_medio_merge_sort:.4f} ms")
    
    # Exibir o tempo em um gráfico usando Seaborn
    sns.set_theme(style="whitegrid")
    sns.lineplot(x=[f"{i+1}" for i in range(num_execucoes)], y=tempos_merge_sort, color="black")
    plt.xlabel('Execuções')
    plt.ylabel('Tempo de Execução (ms)')
    plt.title(f'Tempos de execução do Merge Sort (em {num_execucoes} execuções)')
    plt.show()
