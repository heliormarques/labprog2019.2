
from heapq import heappop, heappush
from collections import defaultdict
INFTO = 1123456789

def dijkstra(s):
    dist[s] = 0
    Q = [(0, s)]
    while Q:
        cost, u = heappop(Q) 
        for i in range(len(LG[u])):
            v = LG[u][i][0] 
            w = LG[u][i][1] 
            if dist[v] > dist[u] + w: 
                dist[v] = dist[u] + w 
                heappush(Q, (dist[v], v)) 

V, E = map(int, input().split())
dist = [INFTO] * V
LG = defaultdict(list)    

for _ in range(E):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    LG[u].append((v, w))
    LG[v].append((u, w))

server = int(input()) - 1
dijkstra(server)
menor = INFTO
maior = -1

for u in range(len(dist)):
    d = dist[u]
    '''print(u+1, dist[u])'''
    if d != 0:
        menor = min(menor, d)
    if d != INFTO:
        maior = max(maior, d)

print(maior - menor)
