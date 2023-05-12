V = float(input())
real = 2.50
total = 0

while V != -1 :
    total += V
    V = float(input())

realTotal = total * real
VicCoins = realTotal / real

print(f"VC$ {VicCoins:.2f}")
print(f"R$ {realTotal:.2f}")
