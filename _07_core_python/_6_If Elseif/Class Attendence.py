a=int(input("Enter total number of working days :"))
b=int(input("Enter total number of days for absent :"))
c=a-b
d=(c/a)*100
print ("your percentage is:",d,"%")
if d>=75:
    print ("your are eligible for exam")
else:
    print ("your are not eligible for exam (fired)")
