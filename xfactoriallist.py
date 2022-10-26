x = int(input("Enter value for x : "))
n = int(input("Enter number of terms :" ))
a,sign = 1,1
lst=[]
for i in range(1,n+1):
    a*=i
    lst.append((x**i/a)*sign)
    sign*=-1
print(lst)