def calculate():
    with open("calculation.txt", "r") as file:
        with open("results.txt", "w") as output:
            for line in file:  # This loops through every line
                parts = line.split()
            
            # Skip empty lines (safety check)
                if len(parts) != 3:
                    output.write(f"{line.strip()} = ERROR\n")
                    continue
            
            first_number = int(parts[0])
            operator = parts[1]
            second_number = int(parts[2])
            
            if operator == "+":
                result = first_number + second_number
            elif operator == "-":
                result = first_number - second_number
            elif operator == "*":
                result = first_number * second_number
            elif operator == "/":
                result = first_number / second_number
            
            output.write(f"{first_number} {operator} {second_number} = {result}\n")

# def main():
#     with open("calculation.txt", "r") as file:

#         for line in file:
#             calculate(line) 








calculate()