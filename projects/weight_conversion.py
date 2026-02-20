weight = float(input("enter your weight: "))
unit = input("kilograms or pounds (K OR L): ")

if unit == "K" :
    weight = weight * 2.205
    unit = "KGS"
    print(f"your weight is {round(weight,3)} {unit} ")
elif unit == "L":
    weight = weight / 2.205
    unit = "LBS"
    print(f"your weight is {round(weight,3)} {unit} ")
else: 
    print(f"{unit} was invalid")

