from itertools import permutations

def distancia(cidade1, cidade2):
    return ((cidade1[0] - cidade2[0])**2 + (cidade1[1] - cidade2[1])**2)**0.5

def calcula_distancia(caminho, cidades):
    distancias = []
    for i in range(len(caminho) - 1):
        cidade_atual = cidades[caminho[i]]
        proxima_cidade = cidades[caminho[i + 1]]
        dist_parcial = distancia(cidade_atual['coordenadas'], proxima_cidade['coordenadas'])
        distancias.append(dist_parcial)
  
    distancias.append(distancia(cidades[caminho[-1]]['coordenadas'], cidades[caminho[0]]['coordenadas']))
    return sum(distancias)

def caixeiro_viajante(cidades):
    num_cidades = len(cidades)
    todas_permutacoes = permutations(range(1, num_cidades))
    todas_permutacoes = [(0,) + permutacao + (0,) for permutacao in todas_permutacoes]
    melhor_caminho = min(todas_permutacoes, key=lambda caminho: calcula_distancia(caminho, cidades))
    menor_distancia = calcula_distancia(melhor_caminho, cidades)
    return melhor_caminho, menor_distancia

cidades_exemplo = {
    0: {'nome': "Cidade A", 'coordenadas': (0, 0)},
    1: {'nome': "Cidade B", 'coordenadas': (4, 5)},
    2: {'nome': "Cidade C", 'coordenadas': (2, 9)},
    3: {'nome': "Cidade D", 'coordenadas': (5, 2)}
}

melhor_caminho, menor_distancia = caixeiro_viajante(list(cidades_exemplo.values()))
print("Melhor caminho:")
for i in range(len(melhor_caminho)):
    cidade_atual = cidades_exemplo[melhor_caminho[i]]
    print(f" {cidade_atual['nome']}", end="")
    if i < len(melhor_caminho) - 1:
        print(" ->", end="")
    else:
        print()

print("\nMenor distância:", menor_distancia)
