
N = int(input("请输入一个正整数N:"))
a = []
while N > 0:
    a.append(N%2)
    N //= 2
a.reverse()
print(''.join(map(str,a)))
