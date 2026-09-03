print("\nWelcome to the area & cost calculator \n")
print("This program will calculate the area and the cost of the area based on the price per meter.\n")

str_length = input("Please type Length \n")
str_width = input("Please type Width \n")
str_meter = input("how much for 1 meter? \n")

float_length = float(str_length)
float_width = float(str_width)
float_meter = float(str_meter)

total_area = float_length * float_width
total_area2 = str(total_area)

print ("Total area is: " + total_area2 + "m²\n")

total_cost = total_area * float_meter
total_cost2 = str(total_cost)

print ("Give the guy: " + total_cost2 + "€" + "\n")

print("Thank you for using the area & cost calculator. Have a great day!\n")
