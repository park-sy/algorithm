# 220208 / 정수론과 조합론 / 1010 / 다리놓기

n = int(input())

for i in range(n):
    b, a = map(int, input().split())


    f = [[0 for _ in range(a+1)] for _ in range(a+1)]
    f[0][0] = 1
    for i in range(1, a+1):
        for j in range(i+1):
            if j == i:
                f[i][j] = 1
            elif j == 0:
                f[i][j] = 1 
            else:
                f[i][j] = f[i-1][j-1] + f[i-1][j]
        
    print(f[a][b]) 