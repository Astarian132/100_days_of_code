import turtle
import random


screen = turtle.Screen()
screen.setup(width=1000, height=600)
user_bet = turtle.textinput(title='Make Your bet', prompt="Which turtle is going to win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def set_up(competitor, y, i):
    competitor.penup()
    competitor.shape('turtle')
    competitor.color(colors[i])
    competitor.setpos(-450, y)


def move_turtle(competitor):
    competitor.fd(random.randint(1, 20))
    if check_pos(competitor):
        return competitor.pencolor()

def check_pos(competitor):
    return (competitor.xcor() > 450)

tim = turtle.Turtle()
tom = turtle.Turtle()
john = turtle.Turtle()
frank = turtle.Turtle()
joe = turtle.Turtle()
fread = turtle.Turtle()
competitors = [tim, tom, john, frank, joe, fread]

i = 0
for competitor in competitors:
    set_up(competitor,y=(250 - (i * 100)), i=i)
    i += 1

winner = None
while winner == None:
    winner = move_turtle(random.choice(competitors))

result = 'Won' if user_bet.lower() == winner.lower() else 'Lost'
print(f"{winner.capitalize()} turtle has won, You've {result}")

screen.exitonclick()
