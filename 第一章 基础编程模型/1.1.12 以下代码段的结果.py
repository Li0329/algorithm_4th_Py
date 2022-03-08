a = []
i = 0
while i < 10:
    a.append(9-i)
    i += 1
print(a)
i = 0
while i < 10:
    a[i] = a[a[i]]
    i += 1
print(a)
for i in range(10):
    print(i)