s = input()
s = s[1: len(s) - 1].split("><")
t = -1
for i in s:
    if i[0] != "/":
        t += 1
        print("  " * t + "<" + i + ">")
    else:
        print("  " * t + "<" + i + ">")
        t -= 1
