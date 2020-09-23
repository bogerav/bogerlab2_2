from random import randint
import turtle
number_of_turtles = 15
steps_of_time_number = 10000
Vx = 200
dt = 0.01
Vy = 200
VxList = []
VyList = []
for i in range (number_of_turtles):
  if (i%2 == 0):
    VxList.append(randint(5, Vx))
    VyList.append(randint(5, Vy))
  else:
    VxList.append(randint(-Vx, -5))
    VyList.append(randint(-Vy, -5))


turtle.speed(0)
turtle.up()
turtle.goto(400, 400)
turtle.down()
turtle.goto(400, -400)
turtle.goto(-400, -400)
turtle.goto(-400, 400)
turtle.goto(400,400)
turtle.up()

pool = [turtle.Turtle(shape="circle") for i in range(number_of_turtles)]

x=0
y=0
count_for_lists = 0
count_unit = 0

for unit in pool:
  unit.shapesize(1,1)
  unit.penup()
  unit.speed(1)
  unit.goto(randint(-400, 400), randint(-400, 400))

for i in range(steps_of_time_number):
  for unit in pool:
    pool_copy = list(pool)
    del pool_copy[count_unit]
    x = unit.xcor()
    y = unit.ycor()
    Vx1 = VxList[count_for_lists]
    Vy1 = VyList[count_for_lists]
    if (y > 400 or y < -400):
      VyList.insert(count_for_lists, -Vy1)
      VyList.pop(count_for_lists + 1)
    if (x < -400 or x > 400):
      VxList.insert(count_for_lists, -Vx1)
      VxList.pop(count_for_lists + 1)
    
    for unit1 in pool_copy:
      if ( abs((x - unit1.xcor())) < 10 and abs((y - unit1.ycor())) < 10):
        VyList.insert(count_for_lists, -Vy1)
        VyList.pop(count_for_lists+1)
        VxList.insert(count_for_lists, -Vx1)
        VxList.pop(count_for_lists+1)
    x += VxList[count_for_lists]*dt
    y += VyList[count_for_lists]*dt
    unit.goto(x,y)
    if (count_for_lists != number_of_turtles - 1):
      count_for_lists+=1
    else:
      count_for_lists = 0
    if (count_unit != number_of_turtles-1):
      count_unit+=1
    else:
      count_unit = 0



