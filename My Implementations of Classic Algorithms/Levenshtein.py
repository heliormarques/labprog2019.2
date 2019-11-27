def levenshtein(dicionario, entrada):
    tamanho = len(dicionario) - len(entrada);
    if tamanho <0:
        tamanho = tamanho * -1;
    if tamanho > 2:
        return None;
    #---------------------------------------------------------------#
    #  uses an auxiliar matrix and memoization on sub-problems      #
    #  in order to solve the bigger problem, (dynamic programming)  #
    #---------------------------------------------------------------#
    distance = [[0 for x in range(len(entrada)+1)] for x in range(len(dicionario)+1)];
    for i in range(len(dicionario)+1): 
        for j in range(len(entrada)+1): 
            if i == 0:
                distance[i][j] = j;
            elif j == 0:
                distance[i][j] = i;
            elif dicionario[i-1] == entrada[j-1]: 
                distance[i][j] = distance[i-1][j-1]; 
            else: 
                distance[i][j] = 1 + min(distance[i][j-1], distance[i-1][j],  distance[i-1][j-1]);
    if distance[len(dicionario)][len(entrada)] <= 2:
        return dicionario;
    else:
        return None;

#######################
entrada = input().split();
dicionario = [None] * int(entrada[0]);
checar = [None] * int(entrada[1]);
for elem in range (int(entrada[0])):
    dicionario[elem] = input();
for elem in range (int(entrada[1])):
    checar[elem] = input();

resultado = ""

temp2 = [];
for palavra in checar:
    for itens in dicionario:
        result = (levenshtein(itens, palavra));
        if result != None:
            temp2.append(result);
    resultado = resultado + (" ".join(temp2));
    temp2 = [];
    resultado += resultado + "/n"
print(resultado)

