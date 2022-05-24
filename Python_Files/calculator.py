print("Select an operation to perform")
print("1 : ADD")
print("2 : SUBTRACT")
print("3 : DIVIDE")
print("4 : MULTIPLY")

operation = input()

if operation == "1":
   num1 = input("Enter the first number  :")
   num2 = input("Enter the second number  :")
   print("The sum is :" + str(int(num1)+int(num2)))
elif operation == "2":
   num1 = input("Enter the first number  :")
   num2 = input("Enter the second number  :")
   print("The difference is :" + str(int(num1)-int(num2)))
elif operation == "3":
   num1 = input("Enter the first number  :")
   num2 = input("Enter the second number  :")
   print("The division is :" + str(int(num1)/int(num2)))
elif operation == "4":
   num1 = input("Enter the first number  :")
   num2 = input("Enter the second number  :")
   print("The product is :" + str(int(num1)*int(num2)))
else:
 print("Invalid Entry")