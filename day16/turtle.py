# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.color("green")
# timmy.shape("turtle")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
from prettytable import PrettyTable
table = PrettyTable()
table.add_column('Pokenmon Name', ['Pikachu','Squirtle','Charmander'])
table.add_column('Type',['Electric','Water','Fire'])
table.header = True
table.align = "l"
print(table)