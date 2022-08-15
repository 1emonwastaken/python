principal = int(input("Enter principal amount : "))
rate = int(input("Enter rate of interest (per annum): "))
time = int(input("Enter time period (in years) : "))
si = (principal*rate*time)/100
print("Simple interest  : ", si)