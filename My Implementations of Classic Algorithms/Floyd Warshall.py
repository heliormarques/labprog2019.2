#number of vertex (N), number of connections(M)
entrada = input().split();
N = int(entrada[0]);
M = int(entrada[1]);

#updated method, using alocation instead of an append in a loop
#although it seems to actually use more memory than the previous code
rows = N;
columns = M;
A = [None] * M;
for elemen in range(M):
    A[elemen] = [int(i) for i in input().split()];

'''
Old method, using append
for i in range(M):
    A.append(list(map(int, input().rstrip().split())));
'''

#matrix alocation
inf = float("inf");
dist = [[inf for x in range(N)] for y in range(N)];

#set distances to the same vertex as 0
for vertex in range(N):
    dist[vertex][vertex] = 0;
    
#set the distances from each vertex to the other
#they are bidirectional.
for vertex in A:
    dist[vertex[0]][vertex[1]] = vertex[2];
    if dist[vertex[1]][vertex[0]] == "inf":
        dist[vertex[1]][vertex[0]] = vertex[2];
    if dist[vertex[1]][vertex[0]] >= vertex[2]:
        dist[vertex[1]][vertex[0]] = vertex[2];

#floyd warshall algorithm
for k in range(N):
    for i in range(N):
        for j in range(N): 
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j];

#result calculation
resultado = float("inf");
for valor in dist:
    if max(valor) <= resultado:
         resultado = max(valor)

print(resultado);
