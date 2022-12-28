a = input("Enter any character : ")
if a >= "A" and a <= "Z":
    print("Entered character is an uppercase alphabet.")
elif a >= "a" and a <= "z":
    print("Entered character is a lowercase alphabet.")
elif a >= "0" and a <= "9":
    print("Entered character is a integer")
else:
    print("Unrecognized character.")  
