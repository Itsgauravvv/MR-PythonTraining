def area_shapes (shape, *args):
    if shape == "circle":
        radius = args[0]
        area = 3.14 * radius ** 2
        return area
    elif shape == "rectangle":
        length = args[0]
        breadth = args[1]
        area = length * breadth
        return area
    elif shape == "triangle":
        base = args[0]
        height = args[1]
        area = 0.5 * base * height
        return area
    else:
        return "Invalid shape"
shape=input("Enter shape (circle, rectangle, triangle): ")
if shape == "circle":
    radius = float(input("Enter radius: "))
    print("Area of circle:", area_shapes(shape, radius))
elif shape == "rectangle":
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))
    print("Area of rectangle:", area_shapes(shape, length, breadth))
elif shape == "triangle":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print("Area of triangle:", area_shapes(shape, base, height))