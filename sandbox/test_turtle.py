from turtle import Turtle, colormode, done


#semi: Turtle = Turtle()
#semi.penup()
#semi.goto(0, 10)
#semi.color("yellow")
#semi.setheading(136)
#semi.pendown()
#semi.begin_fill()
#i: int = 5
#up: int = 40
#while i < 15:
 #   semi.left(i)
  #  semi.forward(up)
   # i += 1

#semi.left(90)
#semi.goto(0, 10)
#semi.end_fill()
#done()

# block: Turtle = Turtle()
# block.goto(-350, 0)
# block.color("#7B98EB")
# block.begin_fill()
# block.speed(30)
# i: int = 0
# side: int = 350
# while i < 4:
#     block.forward(side)
#     block.left(90)
#     i += 1
# block.end_fill()
# done()


# star: Turtle = Turtle()
# star.speed(10)
# star.color("#10B5B5")
# j: int = 0
# star.penup()
# star.goto(0, 100) 
# star.right(90)
# star.pendown()
# up = 100
# star.begin_fill()
# while j < 4:
#     star.forward(up)
#     star.right(135)
#     star.forward(up)
#     star.left(45)
#     j += 1
# star.end_fill()
# done()

# wavy: Turtle = Turtle()
# wavy.speed(30)
# wavy.color("white")
# j: int = 0
# wavy.penup()
# wavy.goto(0, 100) 
# wavy.pendown()
# up = 200
# zigzag: int = 178
# while j < 15:
#     wavy.forward(up)
#     wavy.right(zigzag)
#     up *= .9
#     wavy.forward(up)
#     wavy.left(zigzag)
#     up *= .9
#     j += 1
# done()

jaws: Turtle = Turtle()
jaws.penup()
jaws.goto(0, -100)
jaws.pendown()
jaws.pencolor("black")
jaws.fillcolor("#A5A3B3")
jaws.begin_fill()
i: int = 0
jaws.forward(40)
jaws.left(130)
jaws.forward(40)
jaws.goto(0, -100)
jaws.end_fill
done()
