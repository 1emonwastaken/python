def istrue(x: list):
    for i in x:
        if i == False:
            return False                                         
            break
    else:
        return True


l = eval(input("Enter list"))
for i in range(len(l)):
    for j in range(len(l)):                                       
        print(l[i][j], end = " ")
    print()

lst2=[]                                                           

for k in range(len(l)):                                           
    lst=[]
    for i in range(len(l)):
        for j in range(len(l)):
            if i - j == k or j - i == k:
                if l[i][j] not in lst:
                    lst.append(l[i][j])
    if len(lst)==1:
        lst2.append(True)                                          
    else:
        lst2.append(False)
                                         
print(istrue(lst2))                                                



'''
For matrix of size m x n:
def istrue(l:list)
for i in range(1,len(l)):
    for j in range(1,len(l[0])):
        if l[i][j]==l[i-1][j-1]:
            pass
        else:
            return False
        return True

'''