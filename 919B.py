n = int(input())
c = 10
while n:
    c += 9
    if sum(map(int, str(c))) == 10:
        n -= 1
print(c)
