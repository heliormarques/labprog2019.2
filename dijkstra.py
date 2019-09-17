inf = float("inf");

vetor = {};
vetor['a'] = {};
vetor['a']['b'] = 6;
vetor['a']['d'] = 1;
vetor['b'] = {}
vetor['b']['d'] = 2;
vetor['b']['e'] = 2;
vetor['b']['c'] = 5;
vetor['c'] = {};
vetor['c']['e'] = 5;
vetor['d'] = {};
vetor['d']['e'] = 1;
vetor['e'] = {};

def dijkstra(vetor, start, finish):
    menorCaminho = {}
    anterior = {}
    naoVisto = vetor
    infinity = inf
    path = []

    for node in naoVisto:
        menorCaminho[node] = infinity
    menorCaminho[start] = 0

    while naoVisto:
        minNode = None
        for node in naoVisto:
            if minNode is None:
                minNode = node
            elif menorCaminho[node] < menorCaminho[minNode]:
                minNode = node
        for cam, distance in vetor[minNode].items():
            if distance + menorCaminho[minNode] < menorCaminho[cam]:
                menorCaminho[cam] = distance + menorCaminho[minNode]
                anterior[cam] = minNode
        naoVisto.pop(minNode)
    currentNode = finish
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = anterior[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0,start)
    if menorCaminho[finish] != infinity:
        print(str(menorCaminho[finish]) + " pelo caminho " + str(path))

dijkstra(vetor, 'a', 'c')
