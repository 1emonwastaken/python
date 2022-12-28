#2!-4!+6!...N!
n = int(input("Enter number : "))
sum = 0
sign = 1
for i in range(1,n+1):
    fac=1
    for j in range(1,(2*i)+1):
        fac*=j
    sum+=fac*sign
    sign*=-1
print(sum)
 
