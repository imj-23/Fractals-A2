import turtle
import random

random.seed(17)

hr = turtle.Turtle()
hr.left(90)
hr.speed(150)

def random_color():
    return (random.random(), random.random(), random.random(),)

def tree(length, angle):
    if length < 10: #parameter
        return
    
    else:
        hr.forward(length) 
        
        hr.pencolor(random_color()) #sets a random colour before turning left
        hr.left(angle)
        tree(length * random.uniform(0.6, 0.8), angle - random.randint(5,15)) 

        hr.right(2 * angle)    
        tree(length * random.uniform(0.5, 0.7), angle - random.randint(5,15))  
        
        hr.left(angle)    
        hr.backward(length)

turtle.speed(2)
tree(100, 30)
turtle.exitonclick()


