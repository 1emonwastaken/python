a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
if a>b:
    k = b
else:
    k = a
for i in range(k,a*b):
    if i%a==0 and i%b==0:
        print("The LCM of ", a, "and", b, "is : ", i)
        break
    else:
        continue