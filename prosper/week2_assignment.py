def add (a,b):
	return a + b

def subtration (a,b):
	return a - b

def multiplication (a,b):
	return a * b

def division (a,b):
	if b == 0:
		print(f"Error: {a} is not divisible by {b}")
	return a / b

while True:
	print ("Simple Calculation")
	print("1. Add")
	print("2. Subtraction")
	print("3. Multiplication")
	print("4. Division")

	choice = input("Enter an operator (1 - 4): ")

	while choice == "1" or "2" "3" or "4":
	

		if choice in ["1","2","3","4"]:
			num1 = float(input("Enter the first number: "))
			num2 = float(input("Enter the second number: "))

			if choice == "1":
				result = add(num1,num2)
			elif choice == "2":
				result = subtration(num1,num2)
			elif choice == "3":
				result = multiplication(num1,num2)
			elif choice == "4":
				result = division(num1,num2)

			print("Result:", result)
		
		else:
			print("Error: You entered the wrong number. Please select number (1 - 2)")



