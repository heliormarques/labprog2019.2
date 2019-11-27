#mudar a entrada aqui
lista = [20,5,10,5,15,15,15,5,6,22];

def cortar(lista, corte):
    anterior = '0';
    atual = '0';
    total = 1;
    cortou = False
    for retangulo in lista:
        if retangulo > corte:
            atual = 'acima';
            cortou = True;
        else:
            atual = 'abaixo';

        if atual == 'abaixo' and anterior == 'acima':
            if retangulo <= corte:
                pass
            else:
                total += 1;
        if atual == 'acima' and anterior == 'abaixo':
                total += 1;

        anterior = atual;
    if lista[0] > corte:
        total += 1;
    return total;
resultado = []
for corte in range(len(lista)):
    result = cortar(lista,corte);
    if result is not None:
        resultado.append(result)
print(max(resultado))
