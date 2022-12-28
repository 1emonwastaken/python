
l = eval(input("Enter the list: "))
for j in range(len(l)):                  # with one loop
    print(l[j][j])
     
for i in range(len(l)):                  # with two loops(dont use much)
    for j in range(len(l)):
        if i == j:
            print(l[i][j])
 
