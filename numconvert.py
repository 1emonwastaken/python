while True:
    print("Number Converter: ")
    print("[1] : Decimal to Binary")
    print("[2] : Binary to Decimal")
    print("[3] : Octal to Decimal")
    print("[4] : Exit")
    inp = int(input("Enter the option you require : "))
    if inp == 1:
        dec = int(input("Enter the decimal number to be converted : "))
        print("Binary equivalent of ", dec, "is : ", bin(dec))
    elif inp == 2:
        bnary = int(input("Enter the binary number to be converted : "), 2)
        print("Decimal equivalent of the number is : ", int(bnary))
    elif inp == 3:
        octl = int(input("Enter the octal number to be converted : "), 8)
        print("Decimal equivalent of the number is : ", int(octl))
    elif inp == 4:
        break

