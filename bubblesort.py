list = []
n = int(input("Enter number of terms : "))
for i in range(n):
    list.append(int(input("Enter number : ")))
print(list)
for i in range(n):
    for j in range(n-i-1):
        if list[j]>list[j+1]:
            list[j],list[j+1] = list[j+1],list[j]
    print(list)
