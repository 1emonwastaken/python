n = int(input("Enter the upper limit : "))
m = int(input("Enter number to check divisibility with : "))
print("The numbers divisible by", m, "in the range 1 -", n, "are : ")
for i in range(1,n):
    if i%m==0:
        print(i)
 
