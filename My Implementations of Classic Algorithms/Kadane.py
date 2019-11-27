#Start. Taking initial vars to set matrices sizes
entrada = input().split();
N = int(entrada[0]);
M = int(entrada[1]);
linhas_matrix = int(entrada[2]);
colunas_matrix = int(entrada[3]);


#matrix alocation, both needed;
field = [None] * N;
acumulado = [None] * N;
#Part 1, create a matrix with the board;
    #1.1 empty matrix;
for elemen in range(N):
    field[elemen] = ["None"] * M;
for elemen in range(N):
    acumulado[elemen] = [0] * M;
    #1.2 fill matrix;
for x in range(N):
    local = [int(i) for i in input().split()];
    field[x] = local;
valor_i = 0;
valor_j = 0;
#Kadane's Algorithm, TEST 3;

for i in range(N):
    if (i - 1) < 0:
        valor_i = 0;
    else:
        valor_i = (i - 1);
    for j in range(M):
        if (j - 1) < 0:
            valor_j = 0;
        else:
            valor_j = (j - 1);
        #-------------------------------------------------------------------#
        # Make a matrix with a sum of sub-matrices from (0 to i), (0 to j). #
        # Basically using memoization on a pre-sum of all sub-matrices,     #
        #            using a simple equation on the main matrix.            #
        # This will be used to make sums of all sub-matrices faster         #
        #-------------------------------------------------------------------#
        if i == 0 and j == 0: 
            acumulado[i][j] = field[i][j];
        elif i == 0:
            acumulado[i][j] = acumulado[i][valor_j] + field[i][j];
        elif j == 0:
            acumulado[i][j] = acumulado[valor_i][j] + field[i][j];
        else:
            acumulado[i][j] = acumulado[valor_i][j] + acumulado[i][valor_j] - acumulado[valor_i][valor_j] + field[i][j];

total = 0;
for i in range(N):
    if (i - 1) < 0:
        valor_i = 0;
    else:
        valor_i = (i - 1);
    for j in range(M):
        if (j - 1) < 0:
            valor_j = 0;
        else:
            valor_j = (j - 1);
        #-------------------------------------------------------------------#
        #      Now using two more loops to set my know boundary on the      #
        #            (top)leftmost corner of each iteration.                #
        #   After that, use the previous memoization to calculate the sum   #
        #                       whithin my know boundary                    #
        #-------------------------------------------------------------------#
        linhas_aux = i + linhas_matrix - 1;
        colunas_aux = j + colunas_matrix - 1;
        if linhas_aux >= N or colunas_aux >= M:
            continue;
        if i == 0 and j == 0:
            soma_parcial = acumulado[linhas_aux][colunas_aux];
        elif i == 0:
            soma_parcial = acumulado[linhas_aux][colunas_aux] - acumulado[linhas_aux][valor_j];
        elif j == 0:
            soma_parcial = acumulado[linhas_aux][colunas_aux] - acumulado[valor_i][colunas_aux];
        else:
            soma_parcial = acumulado[linhas_aux][colunas_aux] - acumulado[valor_i][colunas_aux] - acumulado[linhas_aux][valor_j] + acumulado[valor_i][valor_j];
        if total < soma_parcial:
            total = soma_parcial;

print(total);

