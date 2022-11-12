s = input()
crt= 1
ans = 1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        crt+=1
        if crt > ans:
            ans = crt
    else:
        crt=1
print(ans)