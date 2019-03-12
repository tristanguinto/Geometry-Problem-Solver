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

if form.getvalue("v1x") != None:
    v1x = float(form.getvalue("v1x"))
if form.getvalue("v1y") != None:
    v1y = float(form.getvalue("v1y"))
    uVera.append(set_vertex("v1",v1x,v1y))
if form.getvalue("v2x") != None:
    v2x = float(form.getvalue("v2x"))
if form.getvalue("v2y") != None:
    v2y = float(form.getvalue("v2y"))
    uVera.append(set_vertex("v2",v2x,v2y))
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


if form.getvalue("A") != None:
    A = float(form.getvalue("A"))
    uva.append(set_value("A",A))
if form.getvalue("B") != None:
    B = float(form.getvalue("B"))
    uva.append(set_value("B",B))
if form.getvalue("C") != None:
    C = float(form.getvalue("C"))
    uva.append(set_value("C",C))
if form.getvalue("H") != None:
    H = float(form.getvalue("H"))
    uva.append(set_value("H",H))
if form.getvalue("x") != None:
    x = float(form.getvalue("x"))
    uva.append(set_value("x",x))
if form.getvalue("y") != None:
    y = float(form.getvalue("y"))
    uva.append(set_value("y",y))
if form.getvalue("z") != None:
    z = float(form.getvalue("z"))
    uva.append(set_value("z",z))
if form.getvalue("v") != None:
    v = float(form.getvalue("v"))
    uva.append(set_value("v",v))
if form.getvalue("u") != None:
    u = float(form.getvalue("u"))
    uva.append(set_value("u",u))
if form.getvalue("TA") != None:
    TA = float(form.getvalue("TA"))
    uva.append(set_value("TA",TA))

tax = None
tay = None
tbx = None
tby = None
tcx = None
tcy = None
tv1x = None
tv1y = None
tv2x = None
tv2y = None
tl =  None
tlvb = None
tlvc = None
taEdge = None
tbEdge = None
tcEdge = None
tPerim = None
xAngle = None
yAngle = None
zAngle = None
uAngle = None
vAngle = None
tBase = None 
tHeight = None
tArea = None



for x in uVera:
    if x.name == "a":
        tax = x.x
        tay = x.y
    if x.name == "b":
        tbx = x.x
        tby = x.y
    if x.name == "c":
        tcx = x.x
        tcy = x.y
    if x.name == "v1":
        tv1x = x.x
        tv1y = x.y
    if x.name == "v2":
        tv2x = x.x
        tv2y = x.y

    
for x in uva:
    if x.name == "TA":
        tArea = x.value
    if x.name == "A":
        taEdge = x.value
    if x.name == "B":
        tbEdge = x.value
    if x.name == "C":
        tcEdge = x.value
    if x.name == "y":
        yAngle = x.value
    if x.name == "x":
        xAngle = x.value
    if x.name == "z":
        zAngle = x.value
    if x.name == "v":
        vAngle = x.value
    if x.name == "u":
        uAngle = x.value
    if x.name == "H":
        tHeight = x.value


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

print("Content-type:text/html\n")
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
#check coordinates for edge length

if tax != None and tay != None and tbx != None and tby != None and taEdge == None:
    taEdge = distance_form(tax,tay,tbx,tby)
    print("<br> <b>")
    print("You have the coordinates of both a and b! A edge is equal to: ", taEdge)
    print("</b> <br>")
    
if tcx != None and tcy != None and tbx != None and tby != None and tbEdge == None:
    tbEdge = distance_form(tcx,tcy,tbx,tby)
    print("<br> <b>")
    print("You have the coordinates of both c and b! B edge is equal to: ", tbEdge)
    print("</b> <br>")

if tax != None and tay != None and tcx != None and tcy != None and tcEdge == None:
    tcEdge = distance_form(tax,tay,tcx,tcy)
    print("<br> <b>")
    print("You have the coordinates of both a and c! C edge is equal to: ", tcEdge)
    print("</b> <br>")
        
if tv1x != None and tv1y != None and tv2x != None and tv2y != None and tl == None:
    tl = distance_form(tv1x,tv1y,tv2x,tv2y)
    print("<br> <b>")
    print("Line segment length is equal to: ",tl)
    print("</b> <br>")

if tv1x != None and tv1y != None and tbx != None and tby != None and tlvb == None:
    tlvb = distance_form(tv1x,tv1y,tbx,tby)
    print("<br> <b>")
    print("Top mini segment from v1 to b length equal to: ", tlvb)
    print("</b> <br>")

if tv2x != None and tv2y != None and tcx != None and tcy != None and tlvc == None:
    tlvc = distance_form(tv2x,tv2y,tcx,tcy)
    print("<br> <b>")
    print("Bottom mini segment from v2 to c length equal to: ", tlvb)
    print("</b> <br>")

    
#check if all edges are known to find all angles
    
if taEdge != None and tbEdge !=  None and tcEdge != None:
    if zAngle == None:
        zAngle = triangle_cos_angle(taEdge,tcEdge,tbEdge)
        print("<br> <b>")
        print("You have all edges of the triangle! Angle x is equal to: ", zAngle)
        print("</b> <br>")
    if yAngle == None:
        yAngle = triangle_cos_angle(taEdge,tbEdge,tcEdge)
        print("<br> <b>")
        print("You have all edges of the triangle! Angle y is equal to: ", yAngle)
        print("</b> <br>")
    if vAngle == None: 
        vAngle = triangle_cos_angle(tcEdge, tbEdge, taEdge)
        print("<br> <b>")
        print("You have all edges of the triangle! Angle z is equal to :", vAngle)
        print("</b> <br>")

#check for adjacent angles



if xAngle != None and yAngle == None:
    yAngle = adjacent_angle(xAngle)
    print("<br> <b>")
    print("You have an adjacent angle with x and y! y is equal to: ",yAngle)
    print("</b> <br>")

if yAngle != None and xAngle == None:
    xAngle = adjacent_angle(yAngle)
    print("<br> <b>")
    print("You have an adjacent angle with y and x! x is equal to: ",xAngle)
    print("</b> <br>")

if vAngle != None and uAngle == None:
    uAngle = adjacent_angle(vAngle)
    print("<br> <b>")
    print("You have an adjacent angle with v and u! u is equal to: ",uAngle)
    print("</b> <br>")

if uAngle != None and vAngle == None:
    vAngle = adjacent_angle(uAngle)
    print("<br> <b>")
    print("You have an adjacent angle with u and v! v is equal to: ",vAngle)
    print("</b> <br>")

#check if 2 angles are known

if yAngle != None and vAngle != None and zAngle == None:
    zAngle = sum_of_angles(yAngle,vAngle)
    print("<br> <b>")
    print("You have both y and v angles! z is equal to: ",zAngle)
    print("</b> <br>")
    
if yAngle != None and zAngle != None and vAngle == None:
    vAngle = sum_of_angles(yAngle,zAngle)
    print("<br> <b>")
    print("You have both y and z angles! v is equal to: ",vAngle)
    print("</b> <br>")

if yAngle != None and vAngle != None and zAngle == None:
    yAngle = sum_of_angles(zAngle,vAngle)
    print("<br> <b>")
    print("You have both z and v angles! y is equal to: ",yAngle)
    print("</b> <br>")
    
#check if 2 angles and a side are known

if yAngle != None and tcEdge != None and vAngle != None and taEdge == None:
    taEdge = triangle_asa_edge(vAngle,tcEdge,yAngle)
    print("<br> <b>")
    print("Side A is equal to: ",taEdge)
    print("</b> <br>")

if yAngle != None and tcEdge != None and zAngle != None and tbEdge == None:
    tbEdge = triangle_asa_edge(zAngle,tcEdge,yAngle)
    print("<br> <b>")
    print("Side B is equal to: ",tbEdge)
    print("</b> <br>")
    

if vAngle != None and taEdge != None and zAngle != None and tbEdge == None:
    tbEdge = triangle_asa_edge(zAngle,taEdge,vAngle)
    print("<br> <b>")
    print("Side B is equal to: ",tbEdge)
    print("</b> <br>")

if vAngle != None and taEdge != None and yAngle != None and tcEdge == None:
    tcEdge = triangle_asa_edge(yAngle,taEdge,vAngle)
    print("<br> <b>")
    print("Side C is equal to: ",tcEdge)
    print("</b> <br>")

if zAngle != None and tbEdge != None and vAngle != None and taEdge == None:
    taEdge = triangle_asa_edge(vAngle,tbEdge,zAngle)
    print("<br> <b>")
    print("Side A is equal to: ",taEdge)
    print("</b> <br>")

if zAngle != None and tbEdge != None and yAngle != None and tcEdge == None:
    tcEdge = triangle_asa_edge(yAngle,tbEdge,zAngle)
    print("<br> <b>")
    print("Side C is equal to: ",tcEdge)
    print("</b> <br>")
        
#check if all edges are known to find perimeter


if taEdge != None and tbEdge !=  None and tcEdge != None:
    tPerim = triangle_perimeter(taEdge,tbEdge,tcEdge)
    print("<br> <b>")
    print("You have all edges of the triangle! Triangle perimeter is equal to: ", tPerim)
    print("</b> <br>")
    tArea = triangle_heron(taEdge,tbEdge, tcEdge)
    print("<br> <b>")
    print("Area of triangle found by Heron's formula! Triangle area is equal to: ", tArea)
    print("</b> <br>")

#check for base and height to find area


if tbEdge != None and tHeight != None and tArea == None:
    tArea = triangle_area(tbEdge,tHeight)
    print("<br> <b>")
    print("You have base and height so you can find the area of the triangle! Triangle area is equal to: ",tArea)
    print("</b> <br>")



#check if  2 sides and an angle are known for area

if yAngle != None and taEdge != None and tbEdge != None and tArea != None:
    tArea = triangle_sas_area(taEdge, tbEdge, yAngle)
    print("<br> <b>")
    print("Area found through side-angle-side formula! Area is eqaul to: ", tArea)
    print("</b> <br>")
if zAngle != None and taEdge != None and tcEdge != None and tArea != None:
    tArea = triangle_sas_area(taEdge, tcEdge, zAngle)
    print("<br> <b>")
    print("Area found through side-angle-side formula! Area is eqaul to: ", tArea)
    print("</b> <br>")

if vAngle != None and tcEdge != None and tbEdge != None and tArea != None:
    tArea = triangle_sas_area(tcEdge, tbEdge, vAngle)
    print("<br> <b>")
    print("Area found through side-angle-side formula! Area is eqaul to: ", tArea)
    print("</b> <br>")
    


#check for base and area to find height

if tbEdge != None and tArea != None and tHeight == None:
    tHeight = triangle_area_decomp(tArea,tbEdge)
    print("<br> <b>")
    print("You know Area of triangle and its base! Height is equal to: ",tHeight)
    print("</b> <br>")

print("</p>")


print(inputButton)
print("</body>")
print("</html>")

