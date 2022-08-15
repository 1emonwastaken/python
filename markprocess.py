name = input("Enter student name : ")
math = float(input("Enter marks in Mathematics : "))
phy = float(input("Enter marks in Physics : "))
chem = float(input("Enter marks in Chemistry : "))
eng = float(input("Enter marks in English : "))
csi = float(input("Enter marks in Computer Science : "))
total = math + phy + chem + eng + csi 
avg = total / 5
print("Name of candidate : ", name)
print("Total marks : ", total)
print("Average : " , avg)
if avg >= 90:
    print("Grade A " + "\nPass")
elif avg >= 75 and avg < 90:
    print("Grade B " + "\nPass")
elif avg >= 40 and avg < 75:
    print("Grade C " + "\nPass")
else:
    print("Grade D" + "\nFail")