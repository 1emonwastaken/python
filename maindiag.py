'''
1 2 3 4
1 1 1 1
2 3 4 1
4 3 2 1

1 1 4 1




'''
l = eval(input("Enter the list: "))
'''for j in range(len(l)):
    print(l[j][j])'''


    # or 
for i in range(len(l)):
    for j in range(len(l)):
        if i == j:
            print(l[i][j])
