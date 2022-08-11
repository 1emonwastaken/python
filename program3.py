a = float(input("Enter length of first side of triangle : "))
b = float(input("Enter length of second side of triangle : "))
c = float(input("Enter length of third side of triangle : "))
if a+b>c and b+c>a:
	if a+c>b:
		s = (a+b+c)/2
		area = (s*(s-a)*(s-b)*(s-c))**0.5
		print("===================================================================")
		print("Area of triangle = ", area)
else:
	print("Invalid lengths for triangle")
