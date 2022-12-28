n = int(input("Enter number of terms : "))
a,b,sign = 2,9,1
lst = []
for i in range(n):
    lst.append((a/b)*sign)
    a+=3
    b+=4
    sign*=-1
print(lst) 
