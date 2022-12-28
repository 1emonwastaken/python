lst1=eval(input("Enter elements of list 1 : "))
lst2=eval(input("Enter elements of list 2 : "))
lst3=[]
if len(lst1)==len(lst2):
    for i in range(len(lst1)):
        lst3.append(lst1[i]+lst2[i])
else:
    print("Please ensure lists have same number of terms.")
print(lst3)
