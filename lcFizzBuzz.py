n = int(input())
s = []
for i in range(1,n+1):
    if i%3==0 and i%5!=0:
        s.append("Fizz")
    elif i%3!=0 and i%5==0:
        s.append("Buzz")
    elif i%3==0 and i%5==0:
        s.append("FizzBuzz")
    else:
        s.append(str(i))
print(s)