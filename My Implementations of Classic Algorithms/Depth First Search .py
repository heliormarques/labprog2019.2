def dfs(nocorrente, pai, dist, destino):
    if (nocorrente == destino):
        print(dist);
        return True;

    for elemen in grafo[nocorrente]:
        if (elemen != pai):
            if (dfs(elemen, nocorrente, dist + 1, destino)):
                return True;
    return False;

grafo = [];
entrada = input().split();
N, A, B = int(entrada[0]), int(entrada[1]), int(entrada[2]);

grafo = []* N
for i in range(N+1):
    grafo.append([]);

for elemen in range(N-1):
    entrada = input().split();
    i, j = int(entrada[0]), int(entrada[1]);
    grafo[i].append(j);
    grafo[j].append(i);


dfs(A, -1, 0, B);
