def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


a = float(input("Enter the first side length: "))
b = float(input("Enter the second side length: "))
c = float(input("Enter the third side length: "))

if is_a_triangle(a, b, c):
    print("Yes, it can be a triangle.")
else:
    print("No, it cannot be a triangle.")