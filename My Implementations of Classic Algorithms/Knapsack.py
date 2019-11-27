resultado = 0;
peso = [];
valor = [];

entrada = input().split();
capacidade = int(entrada[1]);
itens = int(entrada[0]);


#Updated method, without append
peso = [None] * itens;
valor = [None] * itens;
for vezes in range(int(entrada[0])):
    entrada = input().split();
    peso[vezes] = int(entrada[0]);
    valor[vezes]  = int(entrada[1]);

'''
#old method, using append
for vezes in range(int(entrada[0])):
    entrada = input().split();
    adicionar_peso = int(entrada[0]);
    peso.append(adicionar_peso);
    adicionar_valor = int(entrada[1]);
    valor.append(adicionar_valor);
'''

def roubar(index, capacidade):
    global resultado;
    if index < 0:
        return 0;
    if capacidade == 0:
        return 0;
    if peso[index] > capacidade:
        return roubar(index-1, capacidade);

    #not putting in the bag;
    total_1 = roubar(index-1, capacidade);
    #putting in the bag;
    total_2 = valor[index] + roubar(index -1, capacidade - peso[index]);
    if total_1 >= total_2:
        resultado = total_1;
    else:
        resultado = total_2;
    return resultado;


#precisa chamar a func comecando do ultimo index
print(roubar(itens-1, capacidade));
