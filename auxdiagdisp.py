'''
1 2 3 4
4 3 2 1
1 4 3 2 
3 4 1 2
'''
l = eval(input("Enter list"))
for i in range(len(l)):
    print(l[i][(len(l)-1)-i])

#or

for i in range(len(l)):
    for j in range(len(l)-1,-1,-1):
        if i + j == len(l)-1:
            print(l[i][j])
