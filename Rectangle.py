#Rectangle function
def rectangle(x, y, width, height, pointX, pointY):

    #Convert to integers for math
    x = int(x)
    y = int(y)
    height = int(height)
    width = int(width)
    print(pointX)
    pointX = int(pointX)
    pointY = int(pointY)

    #Define rectangle vertices
    Hrectangle = y + height
    Wrectangle = x + width

    #Print the vertices
    print("Vertex A is (%i, %i), Vertex B is (%i, %i), Vertex C is (%i, %i), Vertex D is (%i, %i)" % (x, y, x, Hrectangle, Wrectangle, Hrectangle, Wrectangle, y))

    #Call the midpoints calculations
    calculate_midpoints(x, y, Hrectangle, Wrectangle, pointX, pointY)

def calculate_midpoints(x, y, Hrectangle, Wrectangle, pointX, pointY):

    #Midpoints calculations
    Fx = x
    FyHyMy = (Hrectangle + y)/2
    Hx = Wrectangle
    IxGxMx = (Wrectangle + x)/2
    Gy = y
    Iy = Hrectangle

    #Determine if the point is on or within the rectangle or on the edge or on a vertex
    if pointX >= x and pointX <= Wrectangle and pointY >= y and pointY <= Hrectangle:
        print("The point (%i, %i) is on or within the rectangle." % (pointX, pointY))

        #Check which quadrant
        if pointX > IxGxMx and pointX < Hx and pointY > FyHyMy and pointY < Iy:
            print("and it is within quadrant 1.")
        elif pointX > Fx and pointX < IxGxMx and pointY > FyHyMy and pointY < Iy:
            print("and it is within quadrant 2.")
        elif pointX > Fx and pointX < IxGxMx and pointY > Gy and pointY < FyHyMy:
            print("and it is within quadrant 3.")
        elif pointX > IxGxMx and pointX < Hx and pointY > Gy and pointY < FyHyMy:
            print("and it is within quadrant 4.")

        #Vertex check
        elif pointX == x and pointY == y:
            print("and it is on vertex A")
        elif pointX == x and pointY == Hrectangle:
            print("and it is on vertex B")
        elif pointX == Wrectangle and pointY == Hrectangle:
            print("and it is on vertex C")
        elif pointX == Wrectangle and pointY == y:
            print("and it is on vertex D")

        #Line check
        elif pointX == x and pointY <= Hrectangle and pointY >= y:
            print("and it is on the line AB")
        elif pointX >= x and pointX <= Wrectangle and pointY == Hrectangle:
            print("and it is on the line BC")
        elif pointX == Wrectangle and pointY <= Hrectangle and pointY >= y:
            print("and it is on the line CD")
        elif pointX >= x and pointX <= Wrectangle and pointY == y:
            print("and it is on the line DA")
    else:
        print("The point (%i, %i) is not on or within the rectangle." % (pointX, pointY))
    #Print midpoints
    print("The midpoints are F(%.2f, %.2f), I(%.2f, %.2f), H(%.2f, %.2f), G(%.2f, %.2f), M(%.2f, %.2f)" %(Fx, FyHyMy, IxGxMx, Iy, Hx, FyHyMy, IxGxMx, Gy, IxGxMx, FyHyMy))

def pinput():
    #Input
    coordinates = input("Enter point in \"(pointX,pointY)\" form(NO SPACES): ")
    bracket1 = coordinates.find("(")
    bracket2 = coordinates.find(")")
    comma = coordinates.find(",")

    if coordinates[0] != "(":
        print("Coordinates must start with (")
        return pinput()

    elif coordinates[-1] != ")":
        print("Coordinates must end with )")
        return pinput()

    elif coordinates.count("(") > 1:
        print("There must only be one (")
        return pinput()

    elif coordinates.count(")") > 1:
        print("There must only be one )")
        return pinput()

    elif comma == -1 or coordinates[bracket1 + 1] == "," or coordinates[bracket2 - 1] == ",":
        print("Comma must be between the 2 integers and there must be only 1 comma")
        return pinput()

    elif coordinates[comma + 1:bracket2] == "":
        print("Must have a second integer")
        return pinput()

    elif coordinates.find(" ") != -1:
        print("There cannot be a space in the coordinates")
        return pinput()

    elif coordinates.count(",") > 1:
        print("There must only be one comma")

    pointX = coordinates[bracket1 + 1:comma]
    pointY = coordinates[comma + 1:bracket2]

    #Check for integer
    if not (pointX.isdigit() and pointY.isdigit()):
        print("Only use integer values")
        return pinput()

    return pointX, pointY

#Assignment
pointX, pointY = pinput()
rectangle(3, 5, 17, 21, pointX, pointY)
