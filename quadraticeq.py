a = float(input("Enter the value of a : "))
b = float(input("Enter the value of b : "))
c = float(input("Enter the value of c : "))
d = b**2 - 4 * a * c
if d > 0:
    root1 = (-b + d ** 0.5)/(2*a)
    root2 = (-b - d **0.5)/(2*a)
    print("First root : ", root1)
    print("Second root : ", root2)
else: 
    print("Unreal roots")