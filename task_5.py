# Task 5: Is a point inside a rectangle?

# Bounds of the rectangle
x0 = 5
x1 = 25
y0 = 20
y1 = 50

# 1. Read x and y coordinates from the user
x = float(input("Enter the x coordinate: "))
y = float(input("Enter the y coordinate: "))

# 2. Inside: strictly between both bounds
if x0 < x < x1 and y0 < y < y1:
    print("Point ({}, {}) is INSIDE the rectangle.".format(x, y))

# 3. Outside: beyond any bound
elif x < x0 or x > x1 or y < y0 or y > y1:
    print("Point ({}, {}) is OUTSIDE the rectangle.".format(x, y))

# 4. Otherwise it must be exactly on an edge
else:
    print("Point ({}, {}) is ON THE BOUNDARY of the rectangle.".format(x, y))