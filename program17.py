gen = input("Enter the sex of the employee (m or f) : ")
sal = int(input("Enter the salary of the employee : "))

if gen == 'm' and sal > 10000:
	bonus = 0.05*sal

elif gen == 'm' and sal <= 10000:
	bonus = 0.07*sal

elif gen == 'f' and sal > 10000:
	bonus = 0.1*sal

else:
	bonus = 0.12*sal

print("===================================================")
print("Total salary with bonus : Rs", sal + bonus)
