entrada = [int(x) for x in input().split(" ")]
numLinha = entrada[0]
numColuna =  entrada[1]
colunas= numColuna +2
matrizs = []
campoBatalha = []


for i in range(numLinha+2):
  matrizs.append(["X"]*colunas)
for x in range(numLinha):
  novaEntrada = input()
  campoBatalha.append(novaEntrada)
for x in range(1,numLinha+1):
  for y in range(1,numColuna+1):
    matrizs[x][y] = campoBatalha[x-1][y-1]


numJogadas = int(input())
for x in range(numJogadas):
  jogadas = [int(x) for x in input().split(" ")]
  linhas = jogadas[0]
  colunas = jogadas[1]
  if matrizs[linhas][colunas] == "#":
    matrizs[linhas][colunas] = "@"



def batalha(linha,coluna,matriz):
    global pedaço_Destruido
    global pedaço_navio
    if matriz[linha][coluna] == "#":
      pedaço_navio +=1
    if matriz[linha][coluna] == ".":
      return
    if matriz[linha][coluna] == "X":
      return
    if matriz[linha][coluna] == "@":
      pedaço_Destruido += 1
      pedaço_navio +=1
    matriz[linha][coluna] = "X"
    batalha(linha-1,coluna,matriz)
    batalha(linha+1,coluna,matriz)
    batalha(linha,coluna-1,matriz) 
    batalha(linha,coluna+1,matriz)


navioDestruido = 0
for i in range(1,numLinha+1):
    for j in range(1,numColuna+1):
      pedaço_navio = 0
      pedaço_Destruido = 0
      if matrizs[i][j] == "@":
        batalha(i,j,matrizs)
        if pedaço_navio == pedaço_Destruido:
          navioDestruido +=1
        navio = 0
        pedaço_Destruido = 0
print(navioDestruido)
