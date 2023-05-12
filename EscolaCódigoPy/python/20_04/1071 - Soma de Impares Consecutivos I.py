x = int(input())
y = int(input())
if x > y:
    z = x
    x = y
    y = z
    
acumuladora = 0
n = x + 1

while n < y:
    if n % 2 == 1:
        acumuladora += n
    n += 1
print(acumuladora)

