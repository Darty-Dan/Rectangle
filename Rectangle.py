#Rectangle function
def rectangle(x, y, height, width, pointX, pointY):

    #Check to make sure everything is a digit
    if not (str(x).isdigit() and str(y).isdigit() and str(height).isdigit() and str(width).isdigit() and str(pointX).isdigit() and str(pointY).isdigit()):
        print("Only use integer values")
        coordinates = input("Enter point in \"(pointX,pointY)\" form: ")
        rectangle(x, y, height, width, pointX, pointY)

    #Convert to integers for math
    x = int(x)
    y = int(y)
    height = int(height)
    width = int(width)
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
    FyHyMy = (Hrectangle + y) / 2
    Hx = Wrectangle
    IxGxMx = (Wrectangle + x) / 2
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
        elif pointX == x and pointY == y:
            print("and it is on vertex A")
        elif pointX == x and pointY == Hrectangle:
            print("and it is on vertex B")
        elif pointX == Wrectangle and pointY == Hrectangle:
            print("and it is on vertex C")
        elif pointX == Wrectangle and pointY == y:
            print("and it is on vertex D")
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

def Pinput():
    #Input
    coordinates = input("Enter point in \"(pointX,pointY)\" form: ")
    bracket1 = coordinates.find("(")
    bracket2 = coordinates.find(")")
    comma = coordinates.find(",")
    #Differentiate all the points needed
    if coordinates[0] != "(":
        print("coordinates must start with (")
        return Pinput()

    if coordinates[-1] != ")":
        print("coordinates must end with )")
        return Pinput()

    if coordinates.count("(") > 1:
        print("There must only be one (")

    if coordinates.count(")") > 1:
        print("there must only be one )")

    if comma == -1 or coordinates[bracket1 + 1] == "," or coordinates[bracket2 - 2] == ",":
        print("Comma must be between the 2 integers and there must be only 1 comma")
        return Pinput()

    if coordinates[comma + 1:bracket2] == "":
        print("Must have a second integer")
        return Pinput()

    pointX = coordinates[bracket1 + 1: comma]
    pointY = coordinates[comma + 1:bracket2]
    return pointX, pointY

pointX, pointY = Pinput()
rectangle(3, 5, 17, 21, pointX, pointY)
