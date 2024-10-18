from turtle import Screen

def create_screen():
    screen = Screen()
    screen.setup(width=600 , height=600)
    screen.title("My snake game")
    screen.tracer(0)
    return screen