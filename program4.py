x1 = float(input("Enter X coordinates of first point : "))
y1 = float(input("Enter Y coordinates of first point : "))
x2 = float(input("Enter X coordinates of second point : "))
y2 = float(input("Enter Y coordinates of second point : "))
d = ((x2-x1)**2 + (y2-y1)**2)**0.5
print("The distance between the two points ","(", x1 , "," , y1, ")", "and ", "(", x2, "," ,y2, ")", "is : ", d)
