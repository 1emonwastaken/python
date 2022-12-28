sum = 0
l = eval(input("Enter list: "))
for i in range(len(l)):
    for j in range(len(l)):
        if i!=(len(l)//2) and j!=(len(l)//2):
            if i == j:
                sum+=l[i][j]
            elif i+j==len(l)-1:
                sum+=l[i][j]
print (sum/(len(l)*2-2))
'''
[[1,2,3,4,5],
[5,4,3,2,1],
[1,3,4,5,2],
[2,3,5,4,1],
[3,4,5,1,2]]
'''
