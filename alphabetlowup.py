ch = input("Enter any alphabet : ")
if ch >= 'A' and ch <= 'Z':
	ch = ch.lower()
	print("The alphabet in lowercase is : ", ch)
else:
	ch = ch.upper()
	print("The alphabet in uppercase is : ", ch)
