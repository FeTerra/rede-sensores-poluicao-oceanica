import math
import matplotlib.pyplot as plt

def distancia_entre_pontos(ponto1, ponto2):
    """
    Calcula a distância euclidiana entre dois pontos no plano.
    
    Args:
    ponto1 (tuple): Coordenadas (x, y) do primeiro ponto.
    ponto2 (tuple): Coordenadas (x, y) do segundo ponto.
    
    Returns:
    float: Distância euclidiana entre os dois pontos.
    """
    x1, y1 = ponto1
    x2, y2 = ponto2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def distribuicao_sensor_otima(pontos, niveis_poluicao):
    """
    Encontra a distribuição ótima dos sensores utilizando programação dinâmica.
    
    Args:
    pontos (list of tuples): Lista de pontos de amostragem.
    niveis_poluicao (list of floats): Lista dos níveis de poluição em cada ponto.
    
    Returns:
    list of int: Índices dos pontos que representam a distribuição ótima dos sensores.
    """
    num_pontos = len(pontos)
    
    # Inicializa a matriz de custos com zeros
    matriz_custos = [[0] * num_pontos for _ in range(num_pontos)]
    
    # Calcula o custo de colocar um sensor em cada ponto
    for i in range(num_pontos):
        for j in range(i + 1, num_pontos):
            distancia = distancia_entre_pontos(pontos[i], pontos[j])
            matriz_custos[i][j] = matriz_custos[j][i] = distancia * niveis_poluicao[j]
    
    # Inicializa a lista para armazenar a distribuição ótima dos sensores
    distribuicao_otima = []
    
    # Implementa a programação dinâmica para encontrar a distribuição ótima
    for i in range(num_pontos):
        custo_minimo = float('inf')
        melhor_sensor = None
        
        for j in range(num_pontos):
            if matriz_custos[i][j] < custo_minimo:
                custo_minimo = matriz_custos[i][j]
                melhor_sensor = j
        
        distribuicao_otima.append(melhor_sensor)
    
    return distribuicao_otima

# Função para plotar os pontos de amostragem com os níveis de poluição
def plotar_pontos(pontos, niveis_poluicao):
    plt.figure(figsize=(8, 6))
    for i, ponto in enumerate(pontos):
        plt.scatter(ponto[0], ponto[1], s=100, label=f"Ponto {i+1}, Poluição: {niveis_poluicao[i]}")
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.title('Pontos de Amostragem com Níveis de Poluição')
    plt.legend()
    plt.grid(True)
    plt.show()

# Exemplo de uso
pontos_amostragem = [(0, 0), (1, 1), (2, 2), (3, 3)]
niveis_poluicao = [0.1, 0.5, 0.8, 0.3]

# Plotar os pontos de amostragem com seus níveis de poluição
plotar_pontos(pontos_amostragem, niveis_poluicao)

# Encontrar a distribuição ótima dos sensores
distribuicao_otima = distribuicao_sensor_otima(pontos_amostragem, niveis_poluicao)
print("Distribuição ótima dos sensores:", distribuicao_otima)
