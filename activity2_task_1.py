# Function 1: find the area of a rectangle
def rectangle_area(length, width):
    area = length * width
    return area


# Function 2: find the total surface area of a box
# A box has 6 faces, in 3 pairs of the same size
def box_surface_area(length, width, height):
    top = rectangle_area(length, width)      # top and bottom
    front = rectangle_area(length, height)    # front and back
    side = rectangle_area(width, height)        # left and right

    total = 2 * top + 2 * front + 2 * side
    return total


# Test the functions
print("Area of rectangle:", rectangle_area(2, 3))
print("Surface area of box:", box_surface_area(2, 3, 4))