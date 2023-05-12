N = 20 *[0]

for i in range(20):
    N[i] = int(input())

i = 0
j = 19 #índice do 20 item

while i < j:
    temp = N[i]
    N[i] = N[j]
    N[j] = temp
    i += 1
    j -= 1

for i in range(20):
    print(f"N[{i}] = {N[i]}")









#i += 1
#j -= 1


#enquanto I < J a sequencia continua
