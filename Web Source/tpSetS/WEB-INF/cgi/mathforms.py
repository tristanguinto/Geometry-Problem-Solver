import math

def set_value(name,value):
    print("You have  assigned " + name + " the value ("+ str(value)+")")
    return u_var(name,value)

def set_vertex(name,x,y):
        print("You have entered " + name + " with coordinates(" + str(x) +"," +str(y)+")" )
        return u_ver(name,x,y)

class vertex:
    def __init__(self,name,x,y):
        self.name = name
        self.x = x
        self.y = y
    
class u_ver:
    def __init__(self,name,x,y):
        self.name = name
        self.x = x
        self.y = y

class u_var:
    def __init__(self,name,value):
        self.name = name
        self.value = value

def sum_of_angles(x,y):
    print("**************SUM OF ANGLES***************")
    print("<br>")
    print("Sum of interior angles fomrula used")
    print("180 = x + y + z")
    print("180 - "+str(x)+" - "+str(y)+" = z")
    return(180 - x - y)


def adjacent_angle(x):
    print("**************ADJACENT ANGLE***************")
    print("<br>")
    print("Adjacent angle formula used")
    print("y = 180 - x")
    print("y = 180 - "+str(x))
    return(180-x)

def triangle_perimeter(x,y,z):
    print("**************PERIMETER OF TRIANGLE***************")
    print("<br>")
    print("Perimeter of triangle formula used")
    print("P = A + B + C")
    print("P = " +str(x)+" + "+str(y)+" + "+str(z))
    return(x+y+z)

def triangle_area(b,h):
    print("**************AREA OF TRIANGLE***************")
    print("<br>")
    print("Area of triangle formula used")
    print("A = (1/2) * b * h")
    print("A = (1/2) *" +str(b)+ " * " +str(h))
    return((1/2)*b*h)

def triangle_heron(a,b,c):
    print("**************HERON'S FORMULA***************")
    print("<br>")
    print("Heron's formula used")
    print("Area can be found if all sides are known")
    print("S = (A+B+C)/2")
    s = (a+b+c)/2
    A = math.sqrt( s*(s-a)*(s-b)*(s-c) )
    print("A = sqrt( S(S-A)(S-B)(S-C) = ",A)

    return( A)


def triangle_sas_area(a,b,c):
    print("**************SIDE ANGLE SIDE FORMULA***************")
    print("<br>")
    print("Area of triangle through side-angle-side formula used")
    print("A = (a * b * sin(C)) / 2")
    return( (a*b* math.sin( math.radians(c) ) ) /2)

def triangle_asa_edge(x,b,y):
    print("**************ANGLE SIDE ANGLE FORMULA***************")
    print("<br>")
    print("a = b * sin(x)/sin(y)")
    return( (b * math.sin(math.radians(x)) ) / math.sin(math.radians(y)) )


def triangle_area_decomp(a,b):
    print("**************DECOMPOSITION OF AREA OF TRIANGLE***************")
    print("<br>")
    print("Decomposition of Triangle Area formula used")
    print("If we know the base and area of a triangle we can find the height")
    print("A = 1/2 * B * H can be rearranged into: H = 2 * A / B")
    return( (2*a)/b )


def triangle_cos_angle(a,b,c):
    print("**************LAW OF COSINES***************")
    print("<br>")
    print("Using law of cosines, we can find find an angle if all side lengths are known")
    print("a^2 + b^2 - 2ab * cos(C) = c^2")
    print("<br>")
    print("Isolate angle C to find the next formula")
    print("cos C = (a^2 + b^2 - c^2)/(2ab) ")
    print("<br>")
    print("C = arccos( ("+str(a)+"^2 + "+str(b)+"^2 -"+str(c)+"^2)/(2*"+str(a)+"*"+str(b)+") )")
    C = math.degrees(math.acos( (a**2 + b**2 - c**2)/(2*a*b) ))
    return(C)

def distance_form(x1,y1,x2,y2):
    print("**************DISTANCE FORMULA***************")
    print("<br>")
    print("Distance formula used")
    print("d = sqrt( (x1-x2)^2 + (y1-y2)^2) )")
    print("d = sqrt( ("+str(x1)+" - "+str(x2)+")^2 + ("+str(y1)+" - "+str(y2)+")^2 )")
    d = float(math.sqrt( (x1-x2)**2 + (y1-y2)**2))
    print("d = ",d)
    return(d) 

def circle_area(r):
    print("**************AREA OF CIRCLE***************")
    print("<br>")
    print("Area of circle formula used")
    print("A = (pi) * r^2")
    print("A = (pi)"+str(r)+"^2")
    return(math.pi * (r **2))

def circle_circle_intersect(x1,x2,d,r1,r2):
    print("**************RADICAL LINE**************")
    print("<br>")
    print("Radical line formula used")
    print("Imagine both circles are on same y axis, meaning the centers only have some x distance between them")
    print("<br>")
    print("Equation of right circle: (x - "+str(x1)+")^2 + (y)^2 = r1^2")
    print("Equation of left circle: (x - "+str(x2)+")^2 + (y)^2 = r2^2")
    print("<br>")
    print("Distance between centers: ",d)
    print("Combine these 2 equations by subtraction of equations to get: (x - "+str(x1)+")^2 + (x - "+str(x2)+")^2 = r1^2 - r2^2")
    print("y is cancelled out")
    print("<br>")
    print("Multiply x formulas to get: (x^2 + 2x"+str(x1)+" + "+str(x1)+"^2) - (x^2 + 2x"+str(x2)+" + "+str(x2)+"^2) = "+str(r1)+"^2 - "+str(r2)+"^2")
    print("<br>")
    print("Rearrange formula so that x is by itself to get: x = ("+str(r1)+"^2 - "+str(r2)+"^2 - "+str(x1)+"^2 + "+str(x2)+"^2) / (2 ("+str(x1)+" - "+str(x2)+")")
    print("<br>")
    print("Find from the original circle formulas that: y^2 = r1^2 - x^2")
    print("<br>")
    print("Use the rearranged formula of x in the this equation to get: y = sqrt[ "+str(r1)+"^2 - ("+str(r1)+"^2 - "+str(r2)+"^2 - "+str(x1)+"^2 + "+str(x2)+"^2) / (2 ("+str(x1)+" - "+str(x2)+")^2 ]")
    print("<br>")
    print("The chord between the 2 intersecting points of the circle is 2 * y")
    print("<br>")
    print("Chord a then equals: 2 * sqrt[] "+str(r1)+"^2 - ("+str(r1)+"^2 - "+str(r2)+"^2 - "+str(x1)+"^2 + "+str(x2)+"^2) / (2 ("+str(x1)+" - "+str(x2)+") ]")
    return( 2 * math.sqrt( r1**2 -( (r1**2 - r2**2 + d**2) / (2*d) )**2) )

def circle_intersect_area(r1,r2,d):
    print("**************INTERSECTING AREA***************")
    print("<br>")
    print("Area of circle intersction formula used")
    print("Use the circular segment formula for both sides in order to find the area of intersction: A(r,d) = r^2 * cos^-1(d/r) - d * sqrt(r^2 - d2)")
    print("Use the distance from the center of the circle to the radical line as d, repeat this for both circles")
    print("This distance is found by this fomurla (Found in when finding the radical line inside the lens): x = (r1^2 - r2^2 - d^2) / (2d)")
    print("<br>")
    print("This distance may be different if the radii of the 2 circles are different")
    d1 = float( (d**2 + r1**2 - r2**2) / (2*d) )
    d2 = float( (d**2 + r2**2 - r1**2) / (2*d) )
    print("d1 = ", d1)
    print("d2 = ", d2)
    print("<br>")
    print("Area for right half: A("+str(r1)+","+str(d1)+") = "+str(r1)+"^2 * cos^-1[ ("+str(d1)+"/"+str(r1)+")] - "+str(d1)+" * sqrt("+str(r1)+"^2 - "+str(d1)+"^2)")
    print("<br>")
    print("Area for left half: A("+str(r2)+","+str(d2)+") = "+str(r2)+"^2 * cos^-1[ ("+str(d2)+"^2 - "+str(r1)+"^2 + "+str(r2)+"^2) / 2 * "+str(d2)+" * "+str(r2)+"] - "+str(d2)+" * sqrt("+str(r2)+"^2 - "+str(d2)+"^2)")
    print("The summation of both halfs equal the total area")
    a1 = (r1**2 * math.acos(d1/r1) ) - (d1 * math.sqrt(r1**2 - d1**2))
    a2 = (r2**2 * math.acos(d2/r2) ) - (d2 * math.sqrt(r2**2 - d2**2))
    return(a1 + a2)

def circle_intersect_points(x1,x2,y1,y2,r1,r2):
    print("**************INTERSECTING POINTS***************")
    print("<br>")
    print("Intersecting points of cirlces formula used")
    print("Take both circles equations and combine them")
    print("<br>")
    print("Equation of right circle: (x - "+str(x1)+")^2 + (y - "+str(y1)+")^2 = r1^2")
    print("Equation of left circle: (x - "+str(x2)+")^2 + (y - "+str(y2)+")^2 = r2^2")
    print("<br>")
    print("Combine these 2 equations by subtraction of equations to get: (x - "+str(x1)+")^2 + (x - "+str(x2)+")^2 = r1^2 - r2^2")
    print("<br>")
    print("Rearrange formula so that x is by itself to get: x = ("+str(r1)+"^2 - "+str(r2)+"^2 - "+str(x1)+"^2 + "+str(x2)+"^2) / (2 ("+str(x1)+" - "+str(x2)+")")
    print("Re enter this formula of x into one of the original circle formulas")
    print("<br>")
    print("Here we are using equation of the right circle:  ( ("+str(r1)+"^2 - "+str(r2)+"^2 - "+str(x1)+"^2 + "+str(x2)+"^2) / (2 ("+str(x1)+" - "+str(x2)+") - "+str(x1)+")^2 + (y)^2 = "+str(r1)+"^2" )
    print("<br>")
    print("Solve for y, giving 2 different y coordinates: y = "+str(y1)+" + sqrt[ ("+str(r1)+"^2 - ( ("+str(r1)+"^2 - "+str(r2)+"^2 - "+str(x1)+"^2 + "+str(x2)+"^2) / (2 ("+str(x1)+" - "+str(x2)+") - "+str(x1)+")^2 ]")
    iy1 = y1 + math.sqrt( r1**2 - ( ((r1**2 - r2**2 - x1**2 + x2**2) / (2*(x2-x1))) - x1)**2 )
    iy2 = y2 - math.sqrt( r1**2 - ( ((r1**2 - r2**2 - x1**2 + x2**2) / (2*(x2-x1))) - x1)**2 )
    print("<br>")
    print("The y coordinates are: iy1 = "+str(iy1)+" and iy2 = "+str(iy2))
    print("Substitute one of the y values to get x, where x is equal to: sqrt( r^2 - y^2 )")
    ix = math.sqrt(r1**2 - iy1**2)
    print("<br>")
    print("<b>Intersecting points of circle are at: ("+str(ix)+","+str(iy1)+") and ("+str(ix)+","+str(iy2)+")</b>")

def circle_intersect_arclen(r1,r2,d):
    print("<br>")
    print("**************ARC LENGTH***************")
    print("<br>")
    print("Arc length of intersecting circles formula used")
    print("Arc length formula is: 2 * pi * r (c/360) where c is the central angle of the arc")
    print("<br>")
    print("To find central angle, we can first find the angle between the distance from the center to the radical line and the radius towards an intersection point")
    print("Distance to radical line is: x = d^2 + r1^2 - r2^2 / 2*d where d is equal to the distance between the centers of the circle")
    print("<br>")
    print("Imagine a right triangle with the radius as hypotenuse, half of the radical line as one edge, and the distance from the center to the radical line as the other edge")
    print("To find the angle we are looking for, use the inverse of cos(x/r)")
    a = math.acos((d**2-r2**2+r1**2)/(2*d*r1))
    a = a*(180/math.pi)
    print("<br>")
    print("Multiply this angle by 2 to get central angle")
    a = 2*a
    print("Use this central angle in the arc length formula from before to get the arc length of the intersecting area")
    return(2*math.pi*r1*(a/360))

def circle_circum(r): 
    print("**************CIRCUMFERENCE***************")
    print("<br>")
    print("Circumference of circle formula used")
    print("C = 2 * (pi) * r")
    print("C = 2 * (pi) * "+str(r))
    return(2*math.pi*r)

def triangle_circle_intersect_arc_area(a,R):
    print("**************CIRCLE TRIANGLE INTERSECTION AREA***************")
    print("<br>")
    print("If we have length of chord a across a circle and radius R, then we can find the area of intersection. ")
    print("We find this by taking the area of the whole sector, and subtracting the triangle underneath the area of intersection. ")
    print("<br>")
    print("r is the distance from the center to the chord, and can be found by this equation, r = 1/2 * sqrt( (4*R^2) - a^2 ). ")
    print("A = R^2 * cos^-1(r/R) - r * sqrt(R^2 - r^2) ")
    r = 1/2*math.sqrt( (4 * R**2) - a**2)
    A = (R**2 * math.acos(r/R) )- (r * math.sqrt(R**2 - r**2) )
    print("<br>")
    print("A = ", A)     
    return( A )

def triangle_circle_intersect_arc_len(a,R):
    print("**************CIRCLE TRIANGLE INTERSECTION AREA***************")
    print("<br>")
    theta = 2 * math.asin(a/(2*R))
    return( R * theta )
    