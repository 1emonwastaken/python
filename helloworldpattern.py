s = "HELLOWORLD"
for i in range(len(s)//2):
    for j in range(i):
        print(" ", end='')
    print(s[i*2], end="")
    for k in range((len(s)-2)-(i*2)):
        print(' ', end ="")
    print(s[i*2+1])




    

