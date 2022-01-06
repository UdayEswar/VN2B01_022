# Range
a = 4
for A in range(1, 6):
    for b in range(1, A):
        print(b,end=' ' )
    print()

n = 4

i = 1
while i <= n:
    j = n
    while j >= i:
        print("*", end=" ")
        j -= 1
    print()
    i += 1



