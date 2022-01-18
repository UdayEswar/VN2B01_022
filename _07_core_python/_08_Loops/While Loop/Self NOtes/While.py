x=int(input("Enter The Value :"))
if x % 5==0:
    print("This Can Div By 5")
else:
    print("This Is Not Module Value Of 5")

i = 1
while i < 5:
    print(i)
    if i==3:
        break
    i = i+1
print("Okay")

i = 0
while i < 5:
    i = i + 1
    if i==3:
        continue
    print(i)


for i in range(65, 90):
    print(char(i), end = " o ")


for Uday in range(5):
    for Vasudev in range(Uday + 1):
        print("*", end = " ")
    print()


for i in range(5):
    for l in range(4-i):
        print("*", end = " ")
    print()

for Uday in range(1):
    for Vasudev in range(9-Uday):
        print("**", end = " ")
    print()






