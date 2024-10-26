import turtle
wn = turtle.Screen()
wn.setup(360,360)
mountainimg = "C:/Users/dakot/source/repos/project3/blockfromarray/Images/mountainsquare.gif"
grassimg = "C:/Users/dakot/source/repos/project3/blockfromarray/Images/grasssquare.gif"
wn.addshape(grassimg)
wn.addshape(mountainimg)
map1 = ["x","x","x","x","x","x",
        "x","y","y","x","y","x",
        "x","y","y","y","y","x",
        "x","y","y","x","x","x",
        "x","x","y","y","y","x",
        "x","x","x","x","x","x"] 
class grass:
    def __init__(self,name,x,y):
        name = turtle.Turtle(shape=grassimg)
        self = name
        self.pu()
        self.speed(0)
        #self.color("green")
        self.setx(x)
        self.sety(y)
class mountain:
    def __init__(self,name,x,y):
        name = turtle.Turtle(shape=mountainimg)
        self = name
        self.pu()
        self.speed(0)
        #self.color("grey")
        self.setx(x)
        self.sety(y)
#global startpointx
#global startpointy


def makemap():
    startpointx = -180/1.75
    startpointy = 180/1.75 #or  startpointy = (wn.window_height()/2)/1.75   or startpointy = wn.window_height()/3.75
    r = -1
    for i in map1:
        p = map1.index(i)
        r +=1
        if r%6==0:
            startpointy-=30
            startpointx = -180/1.75
        startpointx += 30
        if i == "x":
            mountain("mountainblock"+str(p),startpointx,startpointy)
        elif i == "y":
            grass("grassblock"+str(p),startpointx,startpointy)
makemap()
wn.mainloop()

        
