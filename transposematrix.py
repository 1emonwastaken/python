l = [[int(input("E")) for j in range(3)]for i in range(3)]
for i in range(3):
    for j in range(i,3):
        l[i][j],l[j][i] = l[j][i],l[i][j]
print(l) 
