lst1=eval(input("Enter values for list one : "))
lst2=eval(input("Enter values for list two : "))
lst3=[]
for i in lst1:
    if i in lst2:
        lst3.append(i)
    else:
        pass
print(lst3) 