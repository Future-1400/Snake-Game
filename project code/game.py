import turtle
import time
import random
from tkinter import *

Score=0
root=Tk()



exe = turtle.Screen()
exe.title("game")
exe.bgcolor('blue')
exe.setup(width=550,height=500)
exe.tracer(0)


head=turtle.Turtle()
head.speed(0)
head.shape('circle')
head.color('white')
head.penup()
head.goto(0,0)
head.direction='stop'



food=turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('black')
food.penup()
food.goto(0,100)

segments = []





def go_up():
    if head.direction != 'down':
        head.direction='up'
def go_down():
    if head.direction != 'up':
        head.direction='down'
def go_left():
    if head.direction != 'right':
        head.direction='left'
def go_right():
    if head.direction != 'left':
        head.direction='right'



def move():
    if head.direction =='up':
        y=head.ycor()
        head.sety(y+20)
    if head.direction=='down':
        y=head.ycor()
        head.sety(y-20)
    if head.direction=='left':
        x=head.xcor()
        head.setx(x+20)
    if head.direction=='right':
        x=head.xcor()
        head.setx(x-20)


exe.listen()
exe.onkeypress(go_up,'w')
exe.onkeypress(go_up,'W')
exe.onkeypress(go_up,'Up')
exe.onkeypress(go_up,'8')
exe.onkeypress(go_down,'s')
exe.onkeypress(go_down,'S')
exe.onkeypress(go_down,'Down')
exe.onkeypress(go_down,'2')
exe.onkeypress(go_left,'d')
exe.onkeypress(go_left,'D')
exe.onkeypress(go_left,'Right')
exe.onkeypress(go_left,'6')
exe.onkeypress(go_right,'a')
exe.onkeypress(go_right,'A')
exe.onkeypress(go_right,'Left')
exe.onkeypress(go_right,'4')
score=Label(root,text='score =',fg='black')
score.place(relx=0,rely=0)
score_num=Label(root,text=Score,fg='black')
score_num.place(relx=0.425,rely=0)
while True:
    exe.update()


    if head.xcor()>260 or head.xcor()<-260 or head.ycor()<-239.99999999999999 or head.ycor()>239.99999999999999:
        time.sleep(1)
        head.goto(0,0)
        head.direction='stop'
        Game_over=Label(root,text="-----Gameover-----",fg='black')
        Game_over.pack()
        Score=0
        score_num=Label(root,text=Score,fg='black')
        score_num.pack()


        for segment in segments:
            segment.goto(1000,1000)
        
        segments.clear()
        x=random.randint(-257,258)
        y=random.randint(-232,232)
        food.goto(x,y)
    
    if head.distance(food)< 20 :
        Score+=1
        score_num.place(relx=1000,rely=1000)
        score_num=Label(root,text=Score,fg='black')
        score_num.pack()
        x=random.randint(-257,258)
        y=random.randint(-232,232)
        food.goto(x,y)
        new_segment= turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('circle')
        new_segment.color('red')
        new_segment.penup()
        new_segment.goto(0,0)
        segments.append(new_segment)



    for index in range (len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    move()
    for segment in segments:
        if segment.distance(head)<20:
            Game_over=Label(root,text="-----Gameover-----",fg='black')
            Game_over.pack()
            Score=0
            score=Label(root,text='score =',fg='black')
            score.pack()
            score_num=Label(root,text=Score,fg='black')
            score_num.pack()
            time.sleep(2)
            head.goto(0,0)
            head.direction='stop'
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            x=random.randint(-257,258)
            y=random.randint(-232,232)
            food.goto(x,y)

    time.sleep(0.13)

exe.mainloop()
root.mainloop()
