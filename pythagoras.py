a = int(input("Enter the length of side 1 (in units): "))
b = int(input("Enter the length of side 2 (in units): "))
a_squared = a * a
b_squared = b * b
c_squared = a_squared + b_squared
hypotenuse = c_squared ** 0.5
print("Side 1 squared:", a_squared)
print("Side 2 squared:", b_squared)
print("Hypotenuse squared:", c_squared)
print("Hypotenuse:", round(hypotenuse, 2), "units")
