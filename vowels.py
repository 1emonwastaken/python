l = []
n = int(input("Enter number of strings : "))
for i in range(n):
    l.append(input("Enter word : "))
l1 = []
l2 = []
for k in range(len(l)):
    s = 0
    for m in l[k]:
        if m in 'aeiouAEIOU':
            s+=1
    l1+=[s]
max = 0
for j in l1:
    if j > max:
        max = j
for k in range(len(l1)):
    if l1[k]==max:
        print(l[k])