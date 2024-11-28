import turtle
import random

random.seed(40)

hr = turtle.Turtle()
hr.left(90)
hr.speed(150)

def control_direction():
    # Randomly decide whether to turn left or right
    return random.choice(["left", "right"])

def random_color():
    return (random.random(), random.random(), random.random(),)

def tree(length, angle):
    if length < 10: #parameter
        return
    
    else:
        hr.forward(length) 
        
        hr.pencolor(random_color()) #sets a random colour before turning left
        direction = control_direction  

        if direction == "left":
            hr.left(angle)
        else:
            hr.right(angle)
        
        tree(length * random.uniform(0.6, 0.8), angle - random.randint(5,15)) 

        if direction == "left":
            hr.left(2 * angle)
        else:
            hr.right(2 * angle)    

        tree(length * random.uniform(0.5, 0.7), angle - random.randint(5,15))  
        
        if direction == "left":
            hr.left(angle)
        else:
            hr.right(angle)    

        hr.backward(length)

turtle.speed(2)


tree(100, 30)
turtle.exitonclick()


