def f(k):
    s = m = n
    while s > 0 and m:
        l = min(k, m)
        s -= 2 * l
        m -= l
        m -= m // 10
    return s <= 0


n = int(input())
l = [0, n]
while l[1] - l[0] > 1:
    m = sum(l) // 2
    l[f(m)] = m
print(l[1])