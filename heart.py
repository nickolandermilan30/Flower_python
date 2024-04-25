import turtle as pogi
import colorsys as mamamoblue

# Setup turtle screen
pogi.setup(800, 800)
pogi.speed(200)
pogi.tracer(10)
pogi.width(2)
pogi.bgcolor("black")


for j in range(25):
    for i in range(10):
        pogi.color(mamamoblue.hsv_to_rgb(i / 15, j / 25, 1))
        pogi.right(90)
        pogi.circle(200 - j * 4, 90)
        pogi.left(90)
        pogi.circle(200 - j * 4, 90)
        pogi.right(180)
        pogi.circle(50, 24)

pogi.hideturtle()
pogi.done()
