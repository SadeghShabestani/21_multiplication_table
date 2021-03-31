def multiTable():
	n = int(input("Enter Number: "))
	m = int(input("Enter Number: "))

	for i in range(1 , n+1):
		print()
		for j in range(1,m+1):
			print(i * j , end=" ")

print(multiTable())