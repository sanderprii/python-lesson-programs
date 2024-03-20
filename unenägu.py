from turtle import *
from random import randint

unenägu = str(input("Kas sa unenägu mäletad? (jah/ei)"))

def draw_kolmnurk():
    i = 0             
    while i < 3:
        forward(200)
        left(120)
        i = i + 1
    
def draw_ruut():
    i = 0             
    while i < 4:
        forward(100)
        left(90)
        i = i + 1   
    
def draw_ristkülik():
    forward(170)             
    left(90)                
    forward(100)            
    left(90)
    forward(170)
    left(90)
    forward(100)

    
def draw_ring():
    circle(100)
    
if unenägu == "jah":
    
    värv = str(input("Mis värvi unenäomaailm oli?"))
    kuju = str(input("Mis kujuga unenäos olev peategelane oli? (ring, ruut, ristkülik, kolmnurk)"))
    peategelane = str(input("Mis värvi unenäos olev peategelane oli?"))
    
    setup(500, 500)
    speed(300)
    bgcolor(värv)
    begin_fill()
    color(peategelane)
    
    if kuju == "ring":
        draw_ring()
    
    if kuju == "ruut":
        draw_ruut()
    
    if kuju == "ristkülik":
        draw_ristkülik()
    
    if kuju == "kolmnurk":
        draw_kolmnurk()
    
    end_fill()
    exitonclick()




if unenägu == "ei":
    
    
    värvarv = randint(1, 9)
    värvJ = "white"
    if värvarv == 1:
        värvJ = "#660066"
    if värvarv == 2:
        värvJ = "#00ffff"
    if värvarv == 3:
        värvJ = "#00ff00"
    if värvarv == 4:
        värvJ = "#663300"
    if värvarv == 5:
        värvJ = "#9966ff"
    if värvarv == 6:
        värvJ = "#ff9933"
    if värvarv == 7:
        värvJ = "#660033"
    if värvarv == 9:
        värvJ = "#ff99ff"
    peategelaneArv = randint(1,9)
    peategelaneJ = "white"
    if peategelaneArv == 1:
        peategelaneJ = "#99ccff"
    if peategelaneArv == 2:
        peategelaneJ = "#ff99cc"
    if peategelaneArv == 3:
        peategelaneJ = "#ff80bf"
    if peategelaneArv == 4:
        peategelaneJ = "#00cc99"
    if peategelaneArv == 5:
        peategelaneJ = "#e6e6ff"
    if peategelaneArv == 6:
        peategelaneJ = "#00664d"
    if peategelaneArv == 7:
        peategelaneJ = "#666699"
    if peategelaneArv == 9:
        peategelaneJ = "#669999"
    
    setup(500, 500)
    speed(300)
    bgcolor(värvJ)
    begin_fill()
    kujuArv = randint(1,4)
    if kujuArv == 1:
        draw_ring()
    if kujuArv == 2:
        draw_ristkülik()
    if kujuArv == 3:
        draw_ruut()
    if kujuArv == 4:
        draw_kolmnurk()   
    color(peategelaneJ)
    
    end_fill()
    exitonclick()


