N = 10 *[]

v = int(input())
N.append(v)

for i in range(1,10):
    N.append(2* N[i - 1])

for i in range(10):
    print(f"N[{i}] = {N[i]}")


