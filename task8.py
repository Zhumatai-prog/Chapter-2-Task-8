a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def all_numbers(a, b):
	for i in range (b + 1):
		if i >= a:
			print(i)
		

print(all_numbers(a, b))