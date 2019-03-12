#!/usr/bin/python
# Import modules for CGI handling 
import cgi, cgitb 
import math
from mathforms import *

# Create instance of FieldStorage 
form = cgi.FieldStorage() 
cgitb.enable()




uva = []   
uVera = []

if form.getvalue("ax") != None:
    ax = float(form.getvalue("ax"))
if form.getvalue("ay") != None:
    ay = float(form.getvalue("ay"))
    uVera.append(set_vertex("a",ax,ay))
if form.getvalue("bx") != None:
    bx = float(form.getvalue("bx"))
if form.getvalue("by") != None:
    by = float(form.getvalue("by"))
    uVera.append(set_vertex("b",bx,by))
if form.getvalue("cx") != None:
    cx = float(form.getvalue("cx"))
if form.getvalue("cy") != None:
    cy = float(form.getvalue("cy"))
    uVera.append(set_vertex("c",cx,cy))
if form.getvalue("px") != None:
    px = float(form.getvalue("px"))
if form.getvalue("py") != None:
    py = float(form.getvalue("py"))
    uVera.append(set_vertex("p",px,py))
if form.getvalue("ip1x") != None:
    ip1x = float(form.getvalue("ip1x"))
if form.getvalue("ip1y") != None:    
    ip1y = float(form.getvalue("ip1y"))
    uVera.append(set_vertex("ip1",ip1x,ip1y))
if form.getvalue("ip2x") != None:
    ip2x = float(form.getvalue("ip2x"))
if form.getvalue("ip2y") != None:
    ip2y = float(form.getvalue("ip2y"))
    uVera.append(set_vertex("ip2",ip2x,ip2y))
if form.getvalue("ip3x") != None:
    ip3x = float(form.getvalue("ip3x"))
if form.getvalue("ip3y") != None:
    ip3y = float(form.getvalue("ip3y"))
    uVera.append(set_vertex("ip3",ip3x,ip3y))
if form.getvalue("ip4x") != None:
    ip4x = float(form.getvalue("ip4x"))
if form.getvalue("ip4y") != None:
    ip4y = float(form.getvalue("ip4y"))
    uVera.append(set_vertex("ip4",ip4x,ip4y))


if form.getvalue("A") != None:
    A = float(form.getvalue("A"))
    uva.append(set_value("A",A))
if form.getvalue("B") != None:
    B = float(form.getvalue("B"))
    uva.append(set_value("B",B))
if form.getvalue("C") != None:
    C = float(form.getvalue("C"))
    uva.append(set_value("C",C))
if form.getvalue("x") != None:
    x = float(form.getvalue("x"))
    uva.append(set_value("x",x))
if form.getvalue("y") != None:
    y = float(form.getvalue("y"))
    uva.append(set_value("y",y))
if form.getvalue("z") != None:
    z = float(form.getvalue("z"))
    uva.append(set_value("z",z))
if form.getvalue("r") != None:
    r = float(form.getvalue("r"))
    uva.append(set_value("r",r))
if form.getvalue("d") != None:
    d = float(form.getvalue("d"))
    uva.append(set_value("d",d))
if form.getvalue("H") != None:
    H = float(form.getvalue("H"))
    uva.append(set_value("H",H))
if form.getvalue("AC") != None:
    AC = float(form.getvalue("AC"))   
    uva.append(set_value("AC",AC))
if form.getvalue("AT") != None:
    AT = float(form.getvalue("AT"))
    uva.append(set_value("AT",AT))













tcax = None
tcay = None
tcbx = None
tcby = None
tccx = None
tccy = None
ctpx = None
ctpy = None

tcaEdge = None
tcbEdge = None
tccEdge = None
tcPerim = None
tcxAngle = None
tcyAngle = None
tczAngle = None
tcBase = None 
tcHeight = None
tcPerim = None
tcArea = None

ctr = None
ctd = None
ctArea = None
ctCircum = None

tcip1x = None
tcip1y = None
tcip2x  = None
tcip2y = None
tcip3x = None
tcip3y = None
tcip4x = None
tcip4y = None

tcarcl = None
tcarca = None

tcaip1L = None
tcaip2L = None
tccip1L = None
tccip4L = None
tcbip2L = None
tcbip3L = None
tcip3ip4L =  None

tcRArea = None
tcLArea = None
tcTArea = None

for x in uVera:
    if x.name == "a":
        tcax = x.x
        tcay = x.y
    if x.name == "b":
        tcbx = x.x
        tcby = x.y
    if x.name == "c":
        tccx = x.x
        tccy = x.y
    if x.name == "p":
        ctpx = x.x
        ctpy = x.y
    if x.name == "ip1":
        tcip1x = x.x
        tcip1y = x.y
    if x.name == "ip2":
        tcip2x = x.x
        tcip2y = x.y
    if x.name == "ip3":
        tcip3x = x.x
        tcip3y = x.y
    if x.name == "ip4":
        tcip4x = x.x
        tcip4y = x.y


for x in uva:
    if x.name == "AC":
        ctArea = x.value
    if x.name == "AT":
        tcArea = x.value
    if x.name == "r":
        ctr = x.value
    if x.name == "d":
        ctd = x.value
    if x.name == "A":
        tcaEdge = x.value
    if x.name == "B":
        tcbEdge = x.value
    if x.name == "C":
        tccEdge = x.value
    if x.name == "x":
        tcxAngle = x.value
    if x.name == "y":
        tcyAngle = x.value
    if x.name == "z":
        tczAngle = x.value
    if x.name == "H":
        tcHeight = x.value




inputButton = """
<form action='../../index.jsp'>
    <input type = 'submit' name='return' value='Back to main page'>
</form>
"""
style = """<style>
input[type=submit]{
        background-color: #4BB1FF;
        width: 100%;
        padding: 12px 20px;
        margin: 40px 0;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box; 
    }

    
    body{
        background-color: #c1d9ff;
    }

</style>
"""
print("Content-type:text/html")
print("")
print("<html>")
print(style)
print("<title>Results</title>")
print("<body>")
print("<h1>Here are all possible answers</h1>")
print("<h3>You have entered these coordinates</h3>")
print("<ul>")
for x in uVera:
    if x.x != None and x.y != None:
        print("<li>"+x.name+" ("+str(x.x)+","+str(x.y)+") </li>")
print("</ul>")
print("<h3>You have entered these values</h3>")
print("<ul>")
for x in uva:
    if x.value != None:
        print("<li>"+x.name+" = "+str(x.value)+"</li>")
print("</ul>")


#check if any intersetion point is known
i = 1
print("<p>")
if tcip1x != None and tcip1y != None and ctpx != None and ctpy != None and ctr == None:
    print("<br>")
    ctr = distance_form(tcip1x,tcip1y,ctpx,ctpy)

    print("<b>")
    print("You have the center point and a point on the circle! Circle radius is equal to: ", ctr)
    print("</b>")

if tcip2x != None and tcip2y != None and ctpx != None and ctpy != None and ctr == None:
    print("<br>")
    ctr = distance_form(tcip2x,tcip2y,ctpx,ctpy)

    print("<b>")
    print("You have the center point and a point on the circle! Circle radius is equal to: ", ctr)
    print("</b>")

if tcip3x != None and tcip3y != None and ctpx != None and ctpy != None and ctr == None:
    print("<br>")
   
    ctr = distance_form(tcip3x,tcip3y,ctpx,ctpy)

    print("<b>")
    print("You have the center point and a point on the circle! Circle radius is equal to: ", ctr)
    print("</b>")

if tcip4x != None and tcip4y != None and ctpx != None and ctpy != None and ctr == None:
    print("<br>")
    ctr = distance_form(tcip4x,tcip4y,ctpx,ctpy)

    print("<b>")
    print("You have the center point and a point on the circle! Circle radius is equal to: ", ctr)
    print("</b>")

print("</p>")

#check coordinates for edge length
print("<p>")
if tcax != None and tcay != None and tcbx != None and tcby != None and tcaEdge == None:
    print("<br>")
    tcaEdge = distance_form(tcax,tcay,tcbx,tcby)

    print("<b>")
    print("You have the coordinates of both a and b! A edge is equal to: ", tcaEdge)
    print("</b>")

if tccx != None and tccy != None and tcbx != None and tcby != None and tcbEdge == None:
    print("<br>")
    tcbEdge = distance_form(tccx,tccy,tcbx,tcby)

    print("<b>")
    print("You have the coordinates of both c and b! B edge is equal to: ", tcbEdge)
    print("</b>")
    
if tcax != None and tcay != None and tccx != None and tccy != None and tccEdge == None:
    print("<br>")
    tccEdge = distance_form(tcax,tcay,tccx,tccy)

    print("<b>")
    print("You have the coordinates of both a and c! C edge is equal to: ", tccEdge)
    print("</b>")

print("</p>")

#check if 2 angles are known

print("<p>")
if tcyAngle != None and tcxAngle != None and tczAngle == None:
    print("<br>")
    tczAngle = sum_of_angles(tcyAngle,tcxAngle)

    print("<b>")
    print("You have both y and x angles! z is equal to: ",tczAngle)
    print("</b>")

if tcyAngle != None and tczAngle != None and tcxAngle == None:
    print("<br>")
    vAngle = sum_of_angles(yAngle,zAngle)
    print("<b>")
    print("You have both y and z angles! x is equal to: ",tcxAngle)
    print("</b>")


if tczAngle != None and tcxAngle != None and tcyAngle == None:
    print("<br>")
    tcyAngle = sum_of_angles(tczAngle,tcxAngle)

    print("<b>")
    print("You have both z and x angles! y is equal to: ", tcyAngle)
    print("</b>")

print("</p>")

#check if 2 angles and a side are known

print("<p>")
if tczAngle != None and tcaEdge != None and tcxAngle != None and tcbEdge == None:
    print("<br>")
    tcbEdge = triangle_asa_edge(tcxAngle,tcaEdge,tczAngle)

    print("<b>")
    print("Side B is equal to: ",tcbEdge)
    print("</b>")

if tczAngle != None and tcaEdge != None and tcyAngle != None and tccEdge == None:
    print("<br>")
    tccEdge = triangle_asa_edge(tcyAngle,tcaEdge,tczAngle)

    print("<b>")
    print("Side C is equal to: ",tccEdge)
    print("</b>")
    
if tcxAngle != None and tcbEdge != None and tczAngle != None and tcaEdge == None:
    print("<br>")
    tcaEdge = triangle_asa_edge(tczAngle,tcbEdge,tcxAngle)

    print("<b>")
    print("Side A is equal to: ",tcaEdge)
    print("/b>")

if tcxAngle != None and tcbEdge != None and tcyAngle != None and tccEdge == None:
    print("<br>")
    tccEdge = triangle_asa_edge(tcyAngle,tcbEdge,tcxAngle)

    print("<b>")
    print("Side C is equal to: ",tccEdge)
    print("</b>")

if tcyAngle != None and tccEdge != None and tczAngle != None and tcaEdge == None:
    print("<br>")
    tcaEdge = triangle_asa_edge(tczAngle,tccEdge,tcyAngle)

    print("<b>")
    print("Side A is equal to: ",tcaEdge)
    print("</b>")

if tcyAngle != None and tccEdge != None and tcxAngle != None and tcbEdge == None:
    print("<br>")
    tcbEdge = triangle_asa_edge(tcxAngle,tccEdge,tcyAngle)

    print("<b>")
    print("Side B is equal to: ",tcbEdge)
    print("</b>")

print("</p>")

#check if all edges are known to find all angles
    
print("<p>")
if tcaEdge != None and tcbEdge !=  None and tccEdge != None:
    if tcxAngle == None:
        print("<br>")
        tcxAngle = triangle_cos_angle(tcaEdge,tccEdge,tcbEdge)

        print("<b>")
        print("You have all edges of the triangle! Angle x is equal to: ", tcxAngle)
        print("</b>")

    if tcyAngle == None:
        print("<br>")
        tcyAngle = triangle_cos_angle(tcaEdge,tcbEdge,tccEdge)

        print("<b>")
        print("You have all edges of the triangle! Angle y is equal to: ", tcyAngle)
        print("</b>")

    if tczAngle == None:
        print("<br>")
        tczAngle = triangle_cos_angle(tccEdge, tcbEdge, tcaEdge)
        
        print("<b>")
        print("You have all edges of the triangle! Angle z is equal to :", tczAngle)
        print("</b>")

print("</p>")


#check if all edges are known to find perimeter

print("<p>")
if tcaEdge != None and tcbEdge !=  None and tccEdge != None:
    print("<br>")
    tcPerim = triangle_perimeter(tcaEdge,tcbEdge,tccEdge)

    print("<b>")
    print("You have all edges of the triangle! Triangle perimeter is equal to: ", tcPerim)
    print("</b>")
    
    print("<br>")
    tcArea = triangle_heron(tcaEdge,tcbEdge, tccEdge)

    print("<b>")
    print("Area of triangle found by Heron's formula! Triangle area is equal to: ", tcArea)
    print("</b>")

print("</p>")

#check for base and height to find area

print("<p>")
if tcbEdge != None and tcHeight != None and tcArea == None:
    print("<br>")
    tcArea = triangle_area(tcBase,tcHeight)

    print("<b>")
    print("You have base and height so you can find the area of the triangle! Triangle area is equal to: ",tcArea)
    print("</b>")
print("</p>")

#check if  2 sides and an angle are known for area

print("<p>")
if tcyAngle != None and tcaEdge != None and tcbEdge != None and tcArea != None:
    print("<br>")
    tcArea = triangle_sas_area(tcaEdge, tcbEdge, tcyAngle)

    print("<b>")
    print("Area found through side-angle-side formula! Area is eqaul to: ", tcArea)
    print("</b>")

if tczAngle != None and tcbEdge != None and tccEdge != None and tcArea != None:
    print("<br>")
    tcArea = triangle_sas_area(tccEdge, tcbEdge, tczAngle)

    print("<b>")
    print("Area found through side-angle-side formula! Area is eqaul to: ", tcArea)
    print("</b>")
    
if tcxAngle != None and tccEdge != None and tcaEdge != None and tcArea != None:
    print("<br>")
    tcArea = triangle_sas_area(tcaEdge, tccEdge, tcxAngle)

    print("<b>")
    print("Area found through side-angle-side formula! Area is eqaul to: ", tcArea)
    print("</b>")

print("</p>")

#check for base and area to find height

print("<p>")
if tcArea != None and tcbEdge !=None and tcHeight == None:
    print("<br>")
    tcHeight = triangle_area_decomp(tcArea,tcbEdge)

    print("<b>")
    print("Height is equal to: ", tcHeight)
    print("</b>")

print("</p>")

#check if radius or diameter is known

print("<p>")
if ctd != None:
    ctr = c1d/2
    print("<br>")

    print("<b>")
    print("You have the diameter of the circle! Radius of circle is equal to: ", c1r)
    print("</b>")

if ctr != None:
    print("<br>")
    ctArea = circle_area(ctr)

    print("<b>")
    print("Area of circle is equal to: ",ctArea )
    print("</b>")

    print("<br>")
    ctCircum = circle_circum(ctr)

    print("<b>")
    print("Circumference of circle is equal to: ",ctCircum )
    print("</b>")

print("</p>")

#check if intersection points 3 and 4 are known

print("<p>")
if tcip3x != None and tcip3y != None and tcip4x != None and tcip4y != None and ctr != None:
    print("<br>")
    ctipa = distance_form(tcip3x,tcip3y,tcip4x,tcip4y)
    tcarca = triangle_circle_intersect_arc_area(ctipa,ctr)

    print("<b>")
    print("Area of intersection is equal to: ",tcarca)
    print("</b>")

    print("<br>")
    tcarcl = triangle_circle_intersect_arc_len(ctipa, ctr)

    print("<b>")
    print("Arc length of intersection is equal to: ", tcarcl)
    print("</b>")

print("</p>")

    
#check for area of intersection and area of circle known

print("<p>")
if tcarca != None and ctArea != None:
    print("<br>")
    ctAreainTriangle = ctArea - tcarca
    
    print("<b>")
    print("By subtracting the intersection area and area of the circle, the area of circle inside of triangle is equal to: ", ctAreainTriangle)
    print("</b>")

print("</p>")

#check for mini line segments between triangle vertices and intersection

print("<p>")
if tcax != None and tcay != None and tcip1x != None and tcip1y != None:
    print("<br>")
    tcaip1L = distance_form(tcax,tcay,tcip1x,tcip1y)

    print("<b>")
    print("Distance from a to ip1 is equal to: ",tcaip1L)
    print("</b>")

if tcax != None and tcay != None and tcip2x != None and tcip2y != None:
    print("<br>")
    tcaip2L = distance_form(tcax,tcay,tcip2x,tcip2y)

    print("<b>")
    print("Distance from a to ip2 is equal to: ",tcaip2L)
    print("</b>")

if tccx != None and tccy != None and tcip1x != None and tcip1y != None:
    print("<br>")
    tccip1L = distance_form(tccx,tccy,tcip1x,tcip1y)

    print("<b>")
    print("Distance from c to ip1 is equal to: ",tccip1L)
    print("</b>")

if tccx != None and tccy != None and tcip4x != None and tcip4y != None:
    print("<br>")
    tccip4L = distance_form(tccx,tccy,tcip4x,tcip4y)

    print("<b>")
    print("Distance from c to ip4 is equal to: ",tccip4L)
    print("</b>")

if tcbx != None and tcby != None and tcip3x != None and tcip3y != None:
    print("<br>")
    tcbip3L = distance_form(tcbx,tcby,tcip3x,tcip3y)

    print("<b>")
    print("Distance from b to ip3 is equal to: ",tcbip3L)
    print("</b>")

if tcbx != None and tcby != None and tcip2x != None and tcip2y != None:
    print("<br>")
    tcbip2L = distance_form(tcbx,tcby,tcip2x,tcip2y)

    print("<b>")
    print("Distance from b to ip2 is equal to: ",tcbip2L)
    print("</b>")

print("</p>")

#check if ips are known to find areas of triangles subtracted by circle

print("<p>")
if tccip1L != None and tccip4L != None and ctr != None:
    print("<br>")
    tcSAL = distance_form(tcip1x,tcip1y,tcip4x,tcip4y)
    print("<br>")
    tcSA = triangle_circle_intersect_arc_area(tcSAL,ctr)
    print("<br>")
    tcSAT = triangle_heron(tccip1L,tccip4L,tcSAL)
    tcLArea = tcSAT - tcSA

    print("<b>")
    print("By finding the circle segment from ip1 and ip4 and the area of a smaller triangle made from c, ip1, and ip4, the remaining area of the triangle on the left side is equal to: ", tcLArea)
    print("</b>")
    
if tcaip1L != None and tcaip2L != None and ctr != None:
    print("<br>")
    tcSAL = distance_form(tcip1x,tcip1y,tcip2x,tcip2y)
    print("<br>")
    tcSA = triangle_circle_intersect_arc_area(tcSAL,ctr)
    print("<br>")
    tcSAT = triangle_heron(tcaip1L,tcaip2L,tcSAL)
    tcTArea = tcSAT - tcSA

    print("<b>")
    print("By finding the circle segment from ip1 and ip2 and the area of a smaller triangle made from a, ip1, and ip2, the remaining area of the triangle on the top side is equal to: ", tcTArea)
    print("</b>")

if tcbip3L != None and tcbip2L != None and ctr != None:
    print("<br>")
    tcSAL = distance_form(tcip3x,tcip3y,tcip2x,tcip2y)
    print("<br>")
    tcSA = triangle_circle_intersect_arc_area(tcSAL,ctr)
    print("<br>")
    tcSAT = triangle_heron(tcbip3L,tcbip2L,tcSAL)
    tcRArea = tcSAT - tcSA

    print("<b>")
    print("By finding the circle segment from ip3 and ip2 and the area of a smaller triangle made from b, ip3, and ip2, the remaining area of the triangle on the top side is equal to: ", tcRArea)
    print("</b>")

if tcRArea != None and tcTArea != None and tcLArea != None:
    print("<br>")
    tcAreaLeft = tcTArea + tcLArea + tcRArea 
    
    print("<b>")
    print("By adding up all remaing areas, the total area of triangle not inside of the circle is equal to: ",tcAreaLeft)
    print("</b>")

print("</p>")







print(inputButton)
print("</body>")
print("</html>")




