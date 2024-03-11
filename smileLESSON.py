from turtle import *

tuju = input("Mis su tuju on? Vali number (1-5): ")

if tuju == "1":
    # happy face
    color('yellow')
    begin_fill()
    circle(100)  
    end_fill()

    # Esimese silm
    penup()
    goto(-35, 120)  
    pendown()
    color('black')
    begin_fill()
    circle(10)  
    end_fill()

    # Teine silm
    penup()
    goto(35, 120)  
    pendown()
    color('black')
    begin_fill()
    circle(10)  
    end_fill()

    # Suu
    penup()
    goto(-40, 85)  
    pendown()
    color('black')
    width(5)  
    setheading(-60)  
    circle(40, 120)  
    exitonclick()
    
elif tuju == "2":
    color('yellow')
    begin_fill()
    circle(100)  
    end_fill()
 #silmad
    penup() 
    goto(-35, 125)
    pendown()
    color('black')
    begin_fill()
    circle(10)  
    end_fill()

    # teine silm
    penup()
    goto(35, 125)  
    pendown()
    color('black')
    begin_fill()
    circle(10)  
    end_fill()

    # suu
    penup()
    goto(-40, 85)  
    pendown()
    color('black')
    setheading(-120)  
    circle(40, -120)  
elif tuju == "3":
    color('yellow')
    begin_fill()
    circle(100)  
    end_fill()

    #simad
    penup()
    goto(-35, 125)  
    pendown()
    color('black')
    begin_fill()
    circle(10)  
    end_fill()

    penup()
    goto(35, 125) 
    pendown()
    color('black')
    begin_fill()
    circle(10)  
    end_fill()

    # Kulmud
    penup()
    goto(-45, 155)  
    pendown()
    color('black')
    width(5) 
    setheading(-25)  
    forward(30) 

    
    penup()
    goto(15, 155) 
    pendown()
    setheading(25) 
    forward(30)  

    # suu
    penup()
    goto(-40, 75)  
    pendown()
    color('black')
    setheading(-90)  
    circle(40, -180)  
    
elif tuju == "4":
    color('yellow')
    begin_fill()
    circle(100)  
    end_fill()

    penup()
    goto(-35, 125)  
    pendown()
    color('black')
    begin_fill()
    circle(10) 
    end_fill()

    penup()
    goto(35, 125) 
    pendown()
    color('black')
    begin_fill()
    circle(10) 
    end_fill()

    penup()
    goto(-40, 85) 
    pendown()
    color('black')
    setheading(-120)  
    circle(40, -120)  
    
    
    color('blue')
    penup()
    goto(-35, 105)  
    pendown()
    begin_fill()
    circle(5)  
    end_fill()
    penup()
    goto(-45, 85)  
    pendown()
    begin_fill()
    circle(5)  
    end_fill()

    
    penup()
    goto(35, 105)
    pendown()
    begin_fill()
    circle(5)  
    end_fill()
    penup()
    goto(45, 85)  
    pendown()
    begin_fill()
    circle(5) 
    end_fill()
    
elif tuju == "5":
    color('yellow')
    begin_fill()
    circle(100)  
    end_fill()

    penup()
    goto(-35, 125)  
    pendown()
    color('black')
    begin_fill()
    circle(10) 
    end_fill()

    
    penup()
    goto(35, 125)  
    pendown()
    color('black')
    begin_fill()
    circle(10)  
    end_fill()

    penup()
    goto(40, 75)  
    pendown()
    color('black')
    setheading(180)  
    forward(80)
    
tujuParem = input("Kas sinu tuju on paremaks läinud? (yes/no): ")

if tujuParem == "no":
    color('yellow')
    begin_fill()
    circle(100)  
    end_fill()
 #silmad
    penup() 
    goto(-35, 125)
    pendown()
    color('black')
    begin_fill()
    circle(10)  
    end_fill()

    # teine silm
    penup()
    goto(35, 125)  
    pendown()
    color('black')
    begin_fill()
    circle(10)  
    end_fill()

    # suu
    penup()
    goto(-40, 85)  
    pendown()
    color('black')
    setheading(-120)  
    circle(40, -120)
    print("Nii kurb, et ma ei saanud sinu tuju paremaks")
else:
    print("Nii tore kuulda, et su tuju on parem!")
    
hideturtle()
exitonclick()

    

