n = int(input("Enter n: "))
lst = []
for i in range(n):
    x=(2**i)-1
    lst.append(x)
for j in range(len(lst)):
    if j%2==0:
        print(lst[j])
    else: 
        pass