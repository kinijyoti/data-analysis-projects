# Part 1 A -- Make a Line
def make_line(size):
    line = ""
    for i in range(size):
        line +="#"
    return line
print(make_line(5))

# Part 1 B -- Make a Square
# create a function using your make_line function to code a square
def make_square(size):
    square = ""
    for _ in range(size):
       square += make_line (size)
       square += "\n"
    return square

print(make_square(5))


# Part 1 C -- Make a Rectangle

def make_rectangle(width, height):
    rectangle = ""
    for _ in range(height):
        rectangle += (make_line(width) + ("\n"))
    return rectangle
print(make_rectangle(5,3))


# Part 2 A -- Make a Stairs
def make_downward_stairs(height):
    stairs = ""
    for i in range(height):
        stairs += (make_line(i+1) + ("\n"))
    return stairs
print(make_downward_stairs(5))


# Part 2 B -- Make Space-Line 
def make_space_line(numSpaces, numchars):
    space_line = ""
    for i in range(numSpaces):
        space_line += " "
    return space_line + make_line(numchars) + space_line
print(make_space_line(3,5))


# Part 2 C -- Make Isosceles Triangle
def make_isosceles_triangle(height):
    triangle = ""
    for i in range(height):
        triangle += (make_space_line(height -i -1, 2 * i+1) + ("\n"))
    return triangle
print(make_isosceles_triangle(5))


# Part 3 -- Make a Diamond
def make_diamond(height):
    triangle = ""
    for i in range(height):
        triangle += (make_space_line(height -i -1, 2 * i+1) + ("\n"))
    for i in range(height):
        triangle +=(make_space_line(i+1, height-i*2+2) + ("\n"))               

    return triangle

print(make_diamond(5))
