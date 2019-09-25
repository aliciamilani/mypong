# Jucimar Jr 2019
# pong em turtle python https://docs.python.org/3.3/library/turtle.html
# baseado em http://christianthompson.com/node/51
# fonte Press Start 2P https://www.fontspace.com/codeman38/press-start-2p
# som pontuação https://freesound.org/people/Kodack/sounds/258020/

# python mypong.py -1 para modo um jogador
# python mypong.py -2 para modo dois jogadores
import turtle
import os
import sys
import math

player = sys.argv[1]
alt_paddle = 5
larg_paddle = 1

# tamanho(altura) de um segmento da raquete
TAM_UM_SEG = (alt_paddle*10)/4

# desenhar tela
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer()

# desenhar raquete 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("green")
paddle_1.shapesize(stretch_wid=alt_paddle, stretch_len=larg_paddle)
paddle_1.penup()
paddle_1.goto(-350, 0)

# desenhar raquete 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("blue")
paddle_2.shapesize(stretch_wid=alt_paddle, stretch_len=larg_paddle)
paddle_2.penup()
paddle_2.goto(350, 0)

# desenhar bola
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("purple")
ball.penup()
ball.goto(0, 0)
vel = 4
ball.dx = vel * math.cos(math.radians(45))
ball.dy = vel * math.sin(math.radians(45))

# pontuação
score_1 = 0
score_2 = 0

# fonte de vitória
win = turtle.Turtle()
win.speed(0)
win.shape("square")
win.color("white")
win.shapesize(stretch_wid=10, stretch_len=5)
win.penup()
win.hideturtle()
win.goto(0, 0)

# head-up display da pontuação
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 260)
hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))

# movimentação raquete 1
if player != '-1':
    def paddle_1_up():
        y = paddle_1.ycor()
        if y < 250:
            y += 20
        else:
            y = 250
        paddle_1.sety(y)

    def paddle_1_down():
        y = paddle_1.ycor()
        if y > -250:
            y += -20
        else:
            y = -250
        paddle_1.sety(y)


# movimentação raquete 2
def paddle_2_up():
    y = paddle_2.ycor()
    if y < 250:
        y += 20
    else:
        y = 250
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    if y > -250:
        y += -20
    else:
        y = -250
    paddle_2.sety(y)


# ângulo de direção da bola
def direction_angle(angle):
    ball.dx = vel * math.cos(math.radians(angle))
    ball.dy = vel * math.sin(math.radians(angle))


# reiniciando o jogo
def restart():
    paddle_2.goto(350, 0)
    paddle_1.goto(-350, 0)
    ball.goto(0, 0)
    global vel
    vel = 4
    ball.dx = vel * math.cos(math.radians(45))
    ball.dy = vel * math.sin(math.radians(45))
    direction_angle(45)
    hud.clear()
    global score_1
    global score_2
    score_1 = 0
    score_2 = 0
    hud.write("{} : {}".format(score_1, score_2),
              align="center", font=("Press Start 2P", 24, "normal"))


# mapeando as teclas
screen.listen()

if player != '-1':
    screen.onkeypress(paddle_1_up, "w")
    screen.onkeypress(paddle_1_down, "s")
screen.onkeypress(paddle_2_up, "Up")
screen.onkeypress(paddle_2_down, "Down")
screen.onkeypress(restart, "space")

while True:
    screen.update()

    # definindo a posição da raquete2 no modo 1 jogador
    if player == '-1':
        paddle_1.sety(ball.ycor())

    # movimentação da bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # colisão com parede superior
    if ball.ycor() > 290:
        os.system("aplay bounce.wav&")
        ball.sety(290)
        ball.dy *= -1

    # colisão com parede inferior
    if ball.ycor() < -280:
        os.system("aplay bounce.wav&")
        ball.sety(-280)
        ball.dy *= -1

    # colisão com parede esquerda
    if ball.xcor() < -390:
        score_2 += 1
        vel = 4
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2),
                  align="center", font=("Press Start 2P", 24, "normal"))
        os.system("aplay 258020__kodack__arcade-bleep-sound.wav&")
        ball.goto(0, 0)
        direction_angle(45)

    # colisão com parede direita
    if ball.xcor() > 390:
        score_1 += 1
        vel = 4
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2),
                  align="center", font=("Press Start 2P", 24, "normal"))
        os.system("aplay 258020__kodack__arcade-bleep-sound.wav&")
        ball.goto(0, 0)
        direction_angle(45)
        ball.dx *= -1
        ball.dy *= -1

    # colisão com raquete 1
    if ball.xcor() < -330 and ball.ycor() < paddle_1.ycor() + 50 and \
            ball.ycor() > paddle_1.ycor() - 50:
        if ball.ycor() < paddle_1.ycor() + TAM_UM_SEG * 4 and \
                ball.ycor() >= paddle_1.ycor() + TAM_UM_SEG * 3:
            direction_angle(45)
        elif ball.ycor() < paddle_1.ycor() + TAM_UM_SEG * 3 and \
                ball.ycor() >= paddle_1.ycor() + TAM_UM_SEG * 2:
            direction_angle(30)
        elif ball.ycor() < paddle_1.ycor() + TAM_UM_SEG * 2 and \
                ball.ycor() >= paddle_1.ycor() + TAM_UM_SEG * 1:
            direction_angle(15)
        elif ball.ycor() < paddle_1.ycor() + TAM_UM_SEG * 1 and \
                ball.ycor() > paddle_1.ycor() + TAM_UM_SEG * 0:
            direction_angle(5)
        elif ball.ycor() < paddle_1.ycor() + TAM_UM_SEG * 1 and \
                ball.ycor() == paddle_1.ycor() + TAM_UM_SEG * 0:
            direction_angle(0)
        elif ball.ycor() < paddle_1.ycor() + TAM_UM_SEG * 0 and \
                ball.ycor() >= paddle_1.ycor() + TAM_UM_SEG * -1:
            direction_angle(355)
        elif ball.ycor() < paddle_1.ycor() + TAM_UM_SEG * -1 and \
                ball.ycor() >= paddle_1.ycor() + TAM_UM_SEG * -2:
            direction_angle(345)
        elif ball.ycor() < paddle_1.ycor() + TAM_UM_SEG * -2 and \
                ball.ycor() >= paddle_1.ycor() + TAM_UM_SEG * -3:
            direction_angle(330)
        elif ball.ycor() < paddle_1.ycor() + TAM_UM_SEG * -3 and \
                ball.ycor() >= paddle_1.ycor() + TAM_UM_SEG * -4:
            direction_angle(315)
        vel += 1
        os.system("aplay bounce.wav&")

    # colisão com raquete 2
    if ball.xcor() > 330 and ball.ycor() < paddle_2.ycor() + 50 and \
            ball.ycor() > paddle_2.ycor() - 50:
        if ball.ycor() < paddle_2.ycor() + TAM_UM_SEG * 4 and \
                ball.ycor() >= paddle_2.ycor() + TAM_UM_SEG * 3:
            direction_angle(135)
        elif ball.ycor() < paddle_2.ycor() + TAM_UM_SEG * 3 and \
                ball.ycor() >= paddle_2.ycor() + TAM_UM_SEG * 2:
            direction_angle(150)
        elif ball.ycor() < paddle_2.ycor() + TAM_UM_SEG * 2 and \
                ball.ycor() >= paddle_2.ycor() + TAM_UM_SEG * 1:
            direction_angle(165)
        elif ball.ycor() < paddle_2.ycor() + TAM_UM_SEG * 1 and \
                ball.ycor() > paddle_2.ycor() + TAM_UM_SEG * 0:
            direction_angle(175)
        elif ball.ycor() < paddle_2.ycor() + TAM_UM_SEG * 1 and \
                ball.ycor() == paddle_2.ycor() + TAM_UM_SEG * 0:
            direction_angle(180)
        elif ball.ycor() < paddle_2.ycor() + TAM_UM_SEG * 0 and \
                ball.ycor() >= paddle_2.ycor() + TAM_UM_SEG * -1:
            direction_angle(185)
        elif ball.ycor() < paddle_2.ycor() + TAM_UM_SEG * -1 and \
                ball.ycor() >= paddle_2.ycor() + TAM_UM_SEG * -2:
            direction_angle(195)
        elif ball.ycor() < paddle_2.ycor() + TAM_UM_SEG * -2 and \
                ball.ycor() >= paddle_2.ycor() + TAM_UM_SEG * -3:
            direction_angle(210)
        elif ball.ycor() < paddle_2.ycor() + TAM_UM_SEG * -3 and \
                ball.ycor() >= paddle_2.ycor() + TAM_UM_SEG * -4:
            direction_angle(225)
        vel += 1
        os.system("aplay bounce.wav&")

    # condição de vitória
    if score_1 == 5 or score_2 == 5:
        winner = 'player 1' if score_1 > score_2 else 'player 2'
        score_1 = score_2 = 0
        win.write("Victory {}".format(winner), align="center",
                  font=("Press Start 2P", 24, "normal"))
        screen.textinput("Victory {}".format(winner),
                         "Press [ENTER] to restart")
        win.clear()
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=(
            "Press Start 2P", 24, "normal"))
        screen.listen()
