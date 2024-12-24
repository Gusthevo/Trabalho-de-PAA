import time
from quickSort import quick_sort, arrayOrdenado
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
    num_execucoes = 100

    # Lista para armazenar os tempos de execução
    tempos_quick_sort = []

    # Executar o Bubble Sort várias vezes
    for i in range(num_execucoes):
        lista_copia = lista.copy()  # Cria uma cópia da lista original para cada execução
        startTime = time.time()  # Início da medição do tempo
        quick_sort(lista_copia)  # Executar o Quick Sort
        endTime = time.time()  # Fim da medição do tempo

        # Armazenar o tempo de execução em milissegundos
        tempo_execucao = (endTime - startTime) * 1000
        tempos_quick_sort.append(tempo_execucao)


    # Exibir a lista ordenada da última execução
    print("\nLista ordenada da última execução:", arrayOrdenado)
    
    # Calcular o tempo médio
    tempo_medio_quick_sort = sum(tempos_quick_sort) / num_execucoes
    print(f"\nTempo médio do Quick Sort: {tempo_medio_quick_sort:.4f} ms")
    
    # Exibir o tempo em um gráfico usando Seaborn
    sns.lineplot(x=[f"{i+1}" for i in range(num_execucoes)], y=tempo_medio_quick_sort, color = "pink", markers= True)
    plt.xlabel('Execuções')
    plt.ylabel('Tempo de Execução (ms)')
    plt.title(f'Tempos de execução do Quick Sort (em {num_execucoes} execuções)')
    plt.show()
