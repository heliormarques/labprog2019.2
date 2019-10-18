value = []
lista_pings = {};
nao_visitado = [];
################################################################
def shortestpath(ties, ilha, endpoint):
    for valores in ties:
        lista_pings[valores] = 999999999;
        nao_visitado.append(valores);
    lista_pings[ilha] = 0;
    
    while nao_visitado:
        minimo_possivel = min(nao_visitado, key=lambda vertex: lista_pings[vertex]);
        for valores in ties[minimo_possivel]:
            min_path = lista_pings[minimo_possivel] + valores[1];
            if min_path < lista_pings[valores[0]]:
                lista_pings[valores[0]] = min_path;
        nao_visitado.remove(minimo_possivel);
        
    return lista_pings[endpoint];
################################################################

entrada = input().split();
primeiro = int(entrada[0]);
segundo = int(entrada[1]);

ties = {list:[] for list in range(1, (primeiro+1))};

for i in range(segundo):
    a, b, ping = [int(numero) for numero in (input().split())];
    ties[a].append((b, ping));
    ties[b].append((a, ping));
endpoint = (int(input()));

for valores in ties:
    if valores is not endpoint:
        value.append(shortestpath(ties, valores, endpoint));
    else:
        pass;


pingmin = min(value);
pingmax = max(value);
resultado_final = pingmax - pingmin;
print(resultado_final);
