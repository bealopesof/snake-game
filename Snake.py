
# === POSIÇÕES INICIAIS DA COBRA ===
from turtle import Turtle


starting_position = [(0, 0), (-20, 0), (-40, 0)]  # cabeça no (0,0) e dois segmentos atrás
move_distance = 20 

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:


    def __init__(self):
    # === LISTA DE SEGMENTOS DA COBRA ===
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
        

    def create_snake(self):

        # cria os primeiros segmentos da cobra
        for position in starting_position:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")   # cria um quadrado (um pedaço da cobra)
        new_segment.color("white")       # deixa o quadrado branco
        new_segment.penup()              # tira a "caneta" (não deixa rastro)
        new_segment.goto(position)       # coloca o quadrado na posição inicial
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):   # adiciona o quadrado na lista da cobra

        # move cada segmento para onde estava o da frente
        for seg_num in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[seg_num - 1].xcor()  # pega a posição X do segmento da frente
                new_y = self.segments[seg_num - 1].ycor()  # pega a posição Y do segmento da frente
                self.segments[seg_num].goto(new_x, new_y)  # move o segmento atual para onde estava o da frente
                # move a cabeça da cobra
        self.segments[0].forward(move_distance)   # anda para frente


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
           

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
           

   
