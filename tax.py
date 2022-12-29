taxinc = int(input("Enter your income : "))
tax = 0
inc = taxinc - 150000
if inc <= 150000:
    print("No tax")
elif inc >= 150001 and inc < 300000:
    tax = (inc - 150001) * 0.1
elif inc >= 300001 and inc < 500000:
    tax = (inc - 300001) * 0.2    
else: 
    tax = (inc - 500001) * 0.3
print("Tax payable : ", tax)
    
       
