from turtle import Screen
from Snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# === CONFIGURAÇÃO DA TELA ===
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

def jogar():
    global game_is_on, snake, food, score
    snake = Snake()
    food = Food()
    score = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Comer
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.increase_score()

        # Parede
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            score.game_over()

        # Corpo
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                score.game_over()

# --- LOOP PRINCIPAL DO JOGO ---
jogar()

esperando = True
sair = [False]   # truque com lista

def restart():
    global esperando
    esperando = False

def quit_game():
    sair[0] = True
    global esperando
    esperando = False

screen.onkey(restart, "Return")  # ENTER
screen.onkey(quit_game, "q")     # Q para sair

# Mensagem na tela
score.goto(0, -30)
score.write("Pressione ENTER para reiniciar ou Q para sair",
            align="center", font=("Courier", 16, "bold"))

while True:
    esperando = True
    while esperando:  # Espera até apertar ENTER ou Q
        screen.update()
    if sair[0]:
        break
    # Reinicia o jogo
    screen.clear()
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    jogar()
    score.goto(0, -30)
    score.write("Pressione ENTER para reiniciar ou Q para sair",
                align="center", font=("Courier", 16, "bold"))

# Fecha a tela no clique
screen.exitonclick()