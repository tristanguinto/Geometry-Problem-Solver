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



if form.getvalue("p1x") != None:
    p1x = float(form.getvalue("p1x"))
if form.getvalue("p1y") != None:
    p1y = float(form.getvalue("p1y"))
    uVera.append(set_vertex("p1",p1x,p1y))
if form.getvalue("p2x") != None:
    p2x = float(form.getvalue("p2x"))
if form.getvalue("p2y") != None:
    p2y = float(form.getvalue("p2y"))
    uVera.append(set_vertex("p2",p2x,p2y))
if form.getvalue("tipx") != None:
    tipx = float(form.getvalue("tipx"))
if form.getvalue("tipy") != None:
    tipy = float(form.getvalue("tipy"))
    uVera.append(set_vertex("tip",tipx,tipy))
if form.getvalue("bipx") != None:
    bipx = float(form.getvalue("bipx"))
if form.getvalue("bipy") != None:
    bipy = float(form.getvalue("bipy"))
    uVera.append(set_vertex("bip",bipx,bipy))
    
if form.getvalue("r1") != None:
    r1 = float(form.getvalue("r1"))
    uva.append(set_value("r1",r1))
if form.getvalue("r2") != None:
    r2 = float(form.getvalue("r2"))
    uva.append(set_value("r2",r2))
if form.getvalue("d1") != None:
    d1 = float(form.getvalue("d1"))
    uva.append(set_value("d1",d1))
if form.getvalue("x") != None:
    x = float(form.getvalue("x"))
    uva.append(set_value("x",x))
if form.getvalue("d2") != None:
    d2 = float(form.getvalue("d2"))
    uva.append(set_value("d2",d2))
if form.getvalue("lca") != None:
    lca = float(form.getvalue("lca"))
    uva.append(set_value("lca",lca))
if form.getvalue("rca") != None:
    rca = float(form.getvalue("rca"))
    uva.append(set_value("rca",rca))



c1r = None
c2r = None
c1d = None
c2d = None
c1a = None
c2a = None
c1c = None
c2c = None
dbc = None
c1x = None
c1y = None
c2x = None
c2y = None
rl = None
ia = None
iar = None
ial = None
ialr = None
iall = None
lca = None
rca = None
tipx = None
tipy = None
bipx =  None
bipy = None
al1 = None
al2 = None
dbip =  None


for x in uVera:
    if x.name == "p1":
        c1x = x.x
        c1y = x.y
    if x.name == "p2":
        c2x = x.x
        c2y = x.y
    if x.name == "tip":
        tipx = x.x
        tipy = x.y
    if x.name == "bip":
        bipx = x.x
        bipy = x.y



for x in uva:
    if x.name == "rca":
        rca = x.value
    if x.name == "lca":
        lca = x.value
    if x.name == "r1":
        c1r = x.value
    if x.name == "r2":
        c2r = x.value
    if x.name == "d1":
        c1d = x.value
    if x.name == "d2":
        c2d = x.value
    if x.name == "x":
        dbc = x.value


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

print("<p>")



#check if intersection points are known
if c1x != None and c1y != None and tipx != None and tipy != None and c1r == None:
    c1r = distance_form(c1x,c1y,tipx,tipy)
    print("<br> <b>")
    print("You have the center point of the right circle and top intersection point! Radius of the right circle is equal to: ", c1r)
    print("</b> <br>")
if c1x != None and c1y != None and bipx != None and bipy != None and c1r == None:
    c1r = distance_form(c1x,c1y,bipx,bipy)
    print("<br> <b>")
    print("You have the center point of the right circle and bottom intersection point! Radius of the right circle is equal to: ", c1r)
    print("</b> <br>")

    

if c2x != None and c2y != None and tipx != None and tipy != None and c2r == None:
    c2r = distance_form(c2x,c2y,tipx,tipy)
    print("<br> <b>")
    print("You have the center point of the left circle and top intersection point! Radius of the left circle is equal to: ", c2r)
    print("</b> <br>")
if c2x != None and c2y != None and bipx != None and bipy != None and c2r == None:
    c2r = distance_form(c2x,c2y,bipx,bipy)
    print("<br> <b>")
    print("You have the center point of the left circle and bottom intersection point! Radius of the left circle is equal to: ", c2r)
    print("</b> <br>")

if tipx != None and tipy != None and bipx != None and bipy != None:
    dbip = distance_form(tipx,tipy,bipx,bipy)
    print("<br> <b>")
    print("You have both intersection point coordinates! Distance between intersection points is equal to: ", dbip)
    print("</b> <br>")
    
if c1r != None and dbip != None:
    ialr = triangle_circle_intersect_arc_len(dbip,c1r)
    print("<br> <b>")
    print("By using radius of the right circle and distance between intersection points, we can find that the arc length of the interection on its left side is equal to: ", ialr)
    print("</b> <br>")
    ial = triangle_circle_intersect_arc_area(dbip,c1r)
    print("<br> <b>")
    print("Using radius of the right circle and distance between intersection points, we can find the intersction area of the left side! Left side intersection area is equal to: ", ial)
    print("</b> <br>")
    
if c2r != None and dbip != None:
    iall = triangle_circle_intersect_arc_len(dbip,c1r)
    print("<br> <b>")
    print("By using radius of the left circle and distance between intersection points, we can find that the arc length of the interection on its right side is equal to: ", iall)
    print("</b> <br>")
    iar = triangle_circle_intersect_arc_area(dbip,c2r)
    print("<br> <b>")
    print("Using radius of the left circle and distance between intersection points, we can find the intersction area of the right side! Right side intersection area is equal to: ", iar)
    print("</b> <br>")
    
if iar != None and ial != None:
    iat = iar + ial
    print("<br> <b>")
    print("By adding both left and right sides of the intersection area, the total intersection area is equal to: ",iat)
    print("</b> <br>")
    
    
#check if radius or diameter is known

if c1d != None:
    c1r = c1d/2
    print("<br> <b>")
    print("You have the diameter of the right circle! Radius of right circle is equal to: ", c1r)
    print("</b> <br>")
if c2d != None:
    c2r = c2d/2
    print("<br> <b>")
    print("You have the diameter of the left circle! Radius of left circle is equal to: ", c2r)
    print("</b> <br>")
if c1r != None:
    c1a = circle_area(c1r)
    c1c = circle_circum(c1r)
    print("<br> <b>")
    print("You have the radius of the right circle!")
    print("<br>")
    print("Area of right circle is equal to: ",c1a )
    print("<br>")
    print("Circumference of right circle is equal to: ",c1c )
    print("</b> <br>")
if c2r != None:
    c2a = circle_area(c2r)
    c2c = circle_circum(c2r)
    print("<br> <b>")
    print("You have the radius of the left circle!")
    print("<br>")
    print("Area of left circle is equal to: ",c2a )
    print("<br>")
    print("Circumference of left circle is equal to: ",c2c )
    print("</b> <br>")



#check if area is known to get radius and diameter
if lca != None and c2r == None and c2d == None:
    c2r = circle_area_decomp(lca)
    print("<br> <b>")
    print("Radius of left circle is equal to: ",c2r)
    c2d = 2*c2r
    print("<br>")
    print("Diameter of left circle is equal to: ", c2d)
    print("</b> <br>")
    
if rca != None and c1r == None and c1d == None:
    c1r = circle_area_decomp(rca)
    print("<br> <b>")
    print("Radius of right circle is equal to: ",c1r)
    c1d = 2*c1r
    print("<br>")
    print("Diameter of right circle is equal to: ", c1d)
    print("</b> <br>")

        
#check for distance between centers


if c1x != None and c1y != None and c2x != None and c2y != None:
    print("<br> <b>")
    print("Equation of right circle: (x - "+str(c1x)+")^2 + (y-"+str(c1y)+")^2 = r^2")
    print("<br>")
    print("Equation of left circle: (x - "+str(c2x)+")^2 + (y-"+str(c2y)+")^2 = r^2")
    print("</b> <br>")


if dbc == None:
    if c1x != None and c1y != None and c2x != None and c2y != None:
        dbc = distance_form(c1x,c1y,c2x,c2y)
        print("<br> <b>")
        print("You have the coordinates of both centers! Distance between centers is equal to: ", dbc)
        print("</b> <br>")

if dbc != None and c1r != None and c2r != None:
    rl = circle_circle_intersect(c1x,c2x,dbc,c1r,c2r)
    print("<br> <b>")
    print("Intersection chord is equal to: ",rl)
    print("</b> <br>")
    ia = circle_intersect_area(c1r,c2r,dbc)
    print("<br> <b>")
    print("Area of intersection is equal to: ", ia)
    print("</b> <br>")

if c1x != None and c1y != None and c2x != None and c2y != None and c1r != None and c2r != None:
    circle_intersect_points(c1x,c2x,c1y,c2y,c1r,c2r)

if c1r != None and c2r != None and dbc != None:
    al1 = circle_intersect_arclen(c1r,c2r,dbc)
    al2 = circle_intersect_arclen(c2r,c1r,dbc)
    print("<br> <b>")
    print("Arc length of right side: ",al1)
    print("<br> <b>")
    print("Arc length of left side: ",al2)
    print("</b> <br>")




print(inputButton)
print("</body>")
print("</html>")

