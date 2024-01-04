import turtle
bob = turtle.Turtle()

def polygon(t,n,lenght):
    for i in range(n):
        t.fd(lenght)
        t.lt(360/n)


def square(t,tamanho):
    for i in range(4):
        t.fd(tamanho)
        t.lt(90)
square(bob,250)
bob.lt(180)
polygon(bob,360,1)

turtle.mainloop()