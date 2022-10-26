s = input("Enter string")
for i in range(len(s)//2):
    for j in range(i):
        print(" ")
    print(s[i*2])
    for k in range(0,(len(s)-2)-(i*2),-1):
        print(" " )
    print(s[i*2+1])
    print()

    
