operator = input("Enter an operator (+ * / -): ")

num1 = float(input("enter first number: "))
num2 = float(input("enter first number: "))

if operator == "+" :
    result = num1 + num2
    print(round(result,3))
elif operator == "-":
    result = num1 - num2
    print(round(result,3))
elif operator == "/":
   result = num1 / num2
   print(round(result,3))
elif operator == "*":
    result = num1 * num2
    print(round(result,3))
else :
    print(f"{operator} is invalid operator")