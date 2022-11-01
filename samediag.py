def istrue(x: list):
    for i in x:
        if i == False:
            return False                                          #FUNCTION TO CHECK IF ALL DIAGONALS SATISFY CONDITION
            break
    else:
        return True


l = eval(input("Enter list"))
for i in range(len(l)):
    for j in range(len(l)):                                       #PRINTING THE ORIGINAL MATRIX
        print(l[i][j], end = " ")
    print()


lst2=[]                                                           #LIST TO STORE TRUE/FALSE VALUES FOR SAME DIAGONAL

for k in range(len(l)):                                           #CHECKING IF DIAGONALS ARE SAME
    lst=[]
    for i in range(len(l)):
        for j in range(len(l)):
            if i - j == k or j - i == k:
                if l[i][j] not in lst:
                    lst.append(l[i][j])
    if len(lst)==1:
        lst2.append(True)                                          #IF SAME NUMBERS IN ONE DIAGONAL: LST2 HAS TRUE
    else:
        lst2.append(False)                                         #IF SAME NUMBERS NOT IN ONE DIAGONAL: LST2 HAS TRUE
print(istrue(lst2))                                                #IF LST2 HAS ALL TRUE, PROGRAM PRINTS TRUE. IF LST2 HAS EVEN ONE FALSE, PROGRAM PRINTS FALSE


'''
INPUT: 
1 2 3 4 
2 4 2 3
3 2 5 2
4 3 2 6
OUTPUT: FALSE
'''
'''
1 2 3 4
2 1 2 3
3 2 1 2
4 3 2 1
OUTPUT: TRUE
'''