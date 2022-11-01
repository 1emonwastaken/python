prime_list=[]

def isPrime(x: int):
    for k in range(2, int(x**(1/2) + 1)):
        if x % k==0:
            return False
            break
    else:
        return True

l = eval(input("enter list : "))
for i in range(len(l)):
    for j in range(len(l)):
        if i == 0 or j == 0 or i == len(l)-1 or j == len(l)-1:
            print(l[i][j], end = " ")
            if isPrime(l[i][j]) and l[i][j] not in prime_list:
                prime_list.append(l[i][j])

        else:
            print(" ", end = ' ')
    print()
print(prime_list)