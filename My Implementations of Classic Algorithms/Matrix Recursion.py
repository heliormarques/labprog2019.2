def batalha(x_axis, y_axis, matriz):
    global hit_part;
    global hit_and_destroyed;
    global N
    global M
    if matriz[x_axis][y_axis] == "Z":
        return None;
    if matriz[x_axis][y_axis] == ".":
        return None;
    if matriz[x_axis][y_axis] == "#":
        hit_part +=1;
    if matriz[x_axis][y_axis] == "P":
        hit_part +=1;
        hit_and_destroyed += 1;
    matriz[x_axis][y_axis] = "Z";
    #recursive calls
    if (y_axis - 1) >= 0:
        batalha(x_axis, y_axis - 1, matriz);
    if (x_axis - 1) >= 0:
        batalha(x_axis -1, y_axis, matriz);
    if (y_axis + 1) < M:
        batalha(x_axis, y_axis + 1, matriz);
    if (x_axis + 1) < N:
        batalha(x_axis +1, y_axis, matriz);
#func which calculates total hits
def check_intersections(tabuleiro, tiros):
    global total;
    global hit_part;
    global hit_and_destroyed;
    for i in range(N):
        for j in range(M):
            #reset variables
            hit_part = 0;
            hit_and_destroyed = 0;
            if tabuleiro[i][j] == "P":
                #only called if is a hit
                batalha(i, j, tabuleiro);
                if hit_part == hit_and_destroyed:
                    total +=1;
                hit_and_destroyed = 0;
    return(total);

#Start. Taking initial vars to set matrices sizes
entrada = input().split();
N = int(entrada[0]);
M = int(entrada[1]);
hit_part = 0
hit_and_destroyed = 0
total = 0

#matrix alocation, both needed;
tabuleiro = [None] * N;
tiros = ["."] * N;
#Part 1, create a matrix with the board;
    #1.1 empty matrix;
for elemen in range(N):
    tabuleiro[elemen] = ["None"] * M;
    #1.2 fill matrix;
for x in range(N):
    local = list(input());
    tabuleiro[x] = local;
    
#Part 2, create a matrix with the shots taken;
    #2.1 empty matrix;
for elemen in range(N):
    tiros[elemen] = ["."] * M;
    #2.2 fill matrix;
for elemen in range(int(input())):
    local = input().split();
    tiros[(int(local[0]))-1][(int(local[1]))-1] = "T";
    
#Part 3, substitute places in the board where shots hits;
for x in range(N):
    for y in range(M):
        if tabuleiro[x][y] == "#" and tiros[x][y] == "T":
            tabuleiro[x][y] = "P";
#Part 4 function call;
print(check_intersections(tabuleiro, tiros));
