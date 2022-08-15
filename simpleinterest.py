principal = int(input("Enter principal amount : "))
rate = float(input("Enter rate of interest (per annum): "))
time = float(input("Enter time period (in years) : "))
si = (principal*rate*time)/100
print("Simple interest  : ", si)