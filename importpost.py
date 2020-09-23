import turtle as t
All = []

with open('input.txt') as file:
    for line in file:
        A = line.rstrip().split(", ")
        One_of_all = []
        for i in range (0, len(A)-1, 2):
          new = (int(A[i]), int(A[i+1]))
          One_of_all.append(new)
          i+=2
        All.append(One_of_all)

x=0
for i in All:
  t.up()
  t.goto(x, 0)
  for x1,x2 in i:
    t.down()
    t.goto(x1 + x, x2)
  x+=100


