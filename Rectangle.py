#Rectangle function
def rectangle(x, y, width, height, pointX, pointY):

    #Convert to integers for math
    x = int(x)
    y = int(y)
    height = int(height)
    width = int(width)
    pointX = int(pointX)
    pointY = int(pointY)

    #Define for rectangle vertices
    Hrectangle = y + height #Height of rectangle
    Wrectangle = x + width #Width of rectangle

    #Print the vertices
    print("Vertex A is (%i, %i), Vertex B is (%i, %i), Vertex C is (%i, %i), Vertex D is (%i, %i)>" %(x, y, x, Hrectangle, Wrectangle, Hrectangle, Wrectangle, y))

    #Call the midpoints calculations
    calculate_midpoints(x, y, Hrectangle, Wrectangle, pointX, pointY)

def calculate_midpoints(x, y, Hrectangle, Wrectangle, pointX, pointY):
    #Midpoints calculations (Fx = the x cord of point F, FyHyMy = the y cord of point F, H and M)
    Fx = x
    FyHyMy = (Hrectangle + y)/2
    Hx = Wrectangle
    IxGxMx = (Wrectangle + x)/2
    Gy = y
    Iy = Hrectangle

    #Print midpoints
    print("The midpoints are F(%.2f, %.2f), I(%.2f, %.2f), H(%.2f, %.2f), G(%.2f, %.2f), M(%.2f, %.2f)." %(Fx, FyHyMy, IxGxMx, Iy, Hx, FyHyMy, IxGxMx, Gy, IxGxMx, FyHyMy))

    #Determine if the point is on or within the rectangle or on the edge or on a vertex
    if pointX >= x and pointX <= Wrectangle and pointY >= y and pointY <= Hrectangle:
        print("The point (%i, %i) is on or within the rectangle." %(pointX, pointY))

        #Check which quadrant
        if pointX > IxGxMx and pointX < Hx and pointY > FyHyMy and pointY < Iy: #Quadrant 1
            print("and the point (%i, %i) is within quadrant 1." %(pointX, pointY))
        elif pointX > Fx and pointX < IxGxMx and pointY > FyHyMy and pointY < Iy: #Quadrant 2
            print("and the point (%i, %i) is within quadrant 2." %(pointX, pointY))
        elif pointX > Fx and pointX < IxGxMx and pointY > Gy and pointY < FyHyMy: #Quadrant 3
            print("and the point (%i, %i) is within quadrant 3." %(pointX, pointY))
        elif pointX > IxGxMx and pointX < Hx and pointY > Gy and pointY < FyHyMy: #Quadrant 4
            print("and the point (%i, %i) is within quadrant 4." %(pointX, pointY))

        #Between the quadrants
        elif pointX == IxGxMx and pointY > FyHyMy and pointY < Iy: #Quadrant 1, 2
            print("and the point (%i, %i) is between quadrant 1 and 2(I, M)." %(pointX, pointY))
        elif pointX > Fx and pointX < IxGxMx and pointY == FyHyMy: #Quadrant 2, 3
            print("and the point (%i, %i) is between quadrant 2 and 3(F, M)." %(pointX, pointY))
        elif pointX == IxGxMx and pointY > Gy and pointY < FyHyMy: #Quadrant 3, 4
            print("and the point (%i, %i) is between quadrant 3 and 4(M, G)." %(pointX, pointY))
        elif pointX > IxGxMx and pointX < Hx and pointY == FyHyMy: #Quadrant 4, 1
            print("and the point (%i, %i) is between quadrant 4 and 1(M, H)." %(pointX, pointY))

        #Vertex check
        elif pointX == x and pointY == y: #Vertex A
            print("and the point (%i, %i) is on vertex A." %(pointX, pointY))
        elif pointX == x and pointY == Hrectangle: #Vertex B
            print("and the point (%i, %i) is on vertex B." %(pointX, pointY))
        elif pointX == Wrectangle and pointY == Hrectangle: #Vertex C
            print("and the point (%i, %i) is on vertex C." %(pointX, pointY))
        elif pointX == Wrectangle and pointY == y: #Vertex D
            print("and the point (%i, %i) is on vertex D." %(pointX, pointY))

        #Mid-point check
        elif pointX == IxGxMx and pointY == FyHyMy: #Point M
            print("and the point (%i, %i) is on point M and touching all quadrants." %(pointX, pointY))
        elif pointX == Fx and pointY == FyHyMy: #Point F
            print("and the point (%i, %i) is on point F." %(pointX, pointY))
        elif pointX == IxGxMx and pointY == Iy: #Point I
            print("and the point (%i, %i) is on point I." %(pointX, pointY))
        elif pointX == Hx and pointY == FyHyMy: #Point H
            print("and the point (%i, %i) is on point I." %(pointX, pointY))
        elif pointX == IxGxMx and pointY == Gy: #Point G
            print("and the point (%i, %i) is on point G" %(pointX, pointY))

        #Line check
        elif pointX == x and pointY <= Hrectangle and pointY >= y: #AB
            print("and the point (%i, %i) is on the line AB." %(pointX, pointY))
        elif pointX >= x and pointX <= Wrectangle and pointY == Hrectangle: #BC
            print("and the point (%i, %i) is on the line BC.")
        elif pointX == Wrectangle and pointY <= Hrectangle and pointY >= y: #CD
            print("and the point (%i, %i) is on the line CD." %(pointX, pointY))
        elif pointX >= x and pointX <= Wrectangle and pointY == y: #DA
            print("and the point (%i, %i) is on the line DA." %(pointX, pointY))
    else: #Not within rectangle
        print("The point (%i, %i) is not on or within the rectangle." %(pointX, pointY))

def point_input(): #User inputted point

    #Input
    coordinates = input("Enter point in \"(pointX,pointY)\" form(NO SPACES): ")
    #Finding brackets and comma
    bracket1 = coordinates.find("(")
    bracket2 = coordinates.find(")")
    comma = coordinates.find(",")

    #Make sure there is an input
    if coordinates == "":
        print("There must be coordinates inputted")
        return point_input()

    #Make sure there aren't spaces
    elif coordinates.find(" ") != -1:
        print("There cannot be a space in the coordinates")
        return point_input()

    #Check for position of ( and )
    if coordinates[0] != "(" or coordinates[-1] != ")":
        print("Coordinates must start with ( and end with )")
        return point_input()

    #Make sure there is only 1 ( and )
    elif coordinates.count("(") > 1 or coordinates.count(")") > 1:
        print("There must only be one ( and one )")
        return point_input()

    #Make sure there are numbers before the comma and after
    elif coordinates[bracket1 + 1:comma] == "" or coordinates[comma + 1:bracket2] == "":
        print("Must have a first and second integer")
        return point_input()

    #Make sure there is a comma the comma isn't directly after or before the bracket
    elif comma == -1 or coordinates[bracket1 + 1] == "," or coordinates[bracket2 - 1] == ",":
        print("Comma must be between the 2 integers and there must be only 1 comma")
        return point_input()

    #Make sure there is only 1 comma
    elif coordinates.count(",") > 1:
        print("There must only be one comma")
        return point_input()

    #Make sure there are no negatives
    elif coordinates.find("-") != -1:
        print("There must not be any negative numbers")
        return point_input()

    #Defining pointX and pointY
    pointX = coordinates[bracket1 + 1:comma]
    pointY = coordinates[comma + 1:bracket2]

    #Check for integer
    if not (pointX.isdigit() and pointY.isdigit()):
        print("Only use integer values")
        return point_input()

    return pointX, pointY

#Assignment
pointX, pointY = point_input()
rectangle(3, 5, 17, 21, pointX, pointY)
