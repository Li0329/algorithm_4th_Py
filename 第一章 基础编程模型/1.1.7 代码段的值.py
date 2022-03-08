import math
t = 9.0
while abs(t - 9.0//t) > .001:
    t = (9.0//t + t) // 2.0
print("%.5f\n" % t)

sum1 = 0
for i in range(1,1000):
    for j in range(i):
        sum1 += 1
print(sum1)

sum2 = 0
i = 1
while i < 1000:
    i *= 2
    j = 0
    while j < 1000:
        j += 1
        sum2 += 1
print(sum2)
