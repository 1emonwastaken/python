lst = eval(input("Enter integer list : "))
i = 0
sum = 0
while i<len(lst):
    sum+=lst[i]
    i+=1
print("Sum of all elements  : ", sum)