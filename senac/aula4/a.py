import turtle

def draw_background():
    """Desenha uma paisagem com céu, grama e sol."""
    screen = turtle.Screen()
    screen.bgcolor("skyblue")  # Cor do céu

    # Desenhando a grama
    grass = turtle.Turtle()
    grass.penup()
    grass.goto(-400, -100)  # Começa na parte inferior
    grass.pendown()
    grass.color("green")
    grass.begin_fill()
    for _ in range(2):
        grass.forward(800)
        grass.right(90)
        grass.forward(200)
        grass.right(90)
    grass.end_fill()
    grass.hideturtle()

    # Desenhando o sol
    sun = turtle.Turtle()
    sun.penup()
    sun.goto(-300, 200)  # Posição do sol
    sun.pendown()
    sun.color("yellow")
    sun.begin_fill()
    sun.circle(50)  # Raio do sol
    sun.end_fill()
    sun.hideturtle()

    # Desenhando nuvens
    def draw_cloud(x, y):
        cloud = turtle.Turtle()
        cloud.penup()
        cloud.goto(x, y)
        cloud.pendown()
        cloud.color("white")
        cloud.begin_fill()
        for _ in range(6):  # Cada nuvem é composta de 6 círculos
            cloud.circle(20)
            cloud.penup()
            cloud.goto(cloud.xcor() + 30, cloud.ycor() + 10)
            cloud.pendown()
        cloud.end_fill()
        cloud.hideturtle()

    # Criando algumas nuvens
    draw_cloud(100, 150)
    draw_cloud(200, 100)
    draw_cloud(-100, 120)

def draw_heart():
    """Desenha um coração no gramado."""
    pen = turtle.Turtle()
    pen.penup()  # Levanta a caneta para reposicionar
    pen.goto(0, -50)  # Posiciona o coração acima do gramado
    pen.pendown()
    pen.color("red")
    pen.pensize(3)
    pen.speed(5)

    pen.begin_fill()
    pen.left(50)
    pen.forward(133)
    pen.circle(50, 200)
    pen.right(140)
    pen.circle(50, 200)
    pen.forward(133)
    pen.end_fill()

    pen.hideturtle()

# Configurando a tela e desenhando
def main():
    draw_background()
    draw_heart()
    turtle.done()

main()
