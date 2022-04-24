n, m = map(int, input().split())
b = [list(map(int, input().split())) for i in range(n)]
if 1 in b[0] or 1 in b[n - 1]:
    print(2)
else:
    for i in range(n):
        if b[i][0] == 1 or b[i][m - 1] == 1:
            print(2)
            break
        elif i == n - 1:
            print(4)
