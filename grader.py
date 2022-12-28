sub1 = int(input("Enter marks in mathematics: "))
sub2 = int(input("Enter marks in physics : "))
sub3 = int(input("Enter marks in chemistry : "))
sub4 = int(input("Enter marks in computer science : "))
total = sub1 + sub2 + sub3 + sub4 + 0.0
avg = total/4
print("Total marks : ", total )
print("Average : ", avg)
if avg >= 75:
    print("Grade : Distinction")
elif avg >= 60 and avg < 75:
    print("Grade : First Division")
elif avg >= 50 and avg < 60:
    print("Grade : Second Division")
elif avg >= 40 and avg < 50:
    print("Grade : Third Division")
else: 
    print("Fail")
     
