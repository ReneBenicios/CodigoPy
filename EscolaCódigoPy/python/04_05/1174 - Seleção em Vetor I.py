A = 100 * [0]

for i in range(100):
    A[i] = float(input())

for i in range(100):
    if A[i] <= 10:
        print(f"A[{i}] = {A[i]:.1f}")

