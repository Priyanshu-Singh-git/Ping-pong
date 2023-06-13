import turtle
import winsound

class Game():
    def __init__(self):
        self.startscreen__1()
        #self.playbgm()



    def startscreen__1(self):

        self.scrn = turtle.Screen()
        self.scrn.setup(1000, 700)
        self.scrn.bgcolor('grey')
        self.scrn.title('Ping Pong')
        self.scrn.tracer(0)

        self.pen=turtle.Turtle()
        self.pen.color('white')
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(-100, 300)
        self.pen.color('red')
        self.pen.write('PING PONG', font=("Ariel", 30, "normal"))

        self.pen.goto(120,-50)
        self.pen.pendown()
        self.pen.color('cyan')
        for i in range(4):
            self.pen.begin_fill()
            self.pen.lt(90)
            self.pen.forward(70)
            self.pen.lt(90)
            self.pen.forward(200)
            self.pen.end_fill()
        self.pen.penup()
        self.pen.goto(0,-25)
        self.pen.color('blue')
        self.pen.write('Start',font=('Ariel',20,"normal"))


        self.pen.goto(self.pen.xcor()+10,self.pen.ycor()-25)
        self.pen.color('black')
        self.pen.write("PRESS S")
        self.scrn.listen()
        self.scrn.onkeypress(self.mainscreen__2, "s")

    def mainscreen__2(self):
        self.pen.clear()
        self.scrn.bgcolor('black')


        self.p1=turtle.Turtle()
        self.p2=turtle.Turtle()



        self.p1.shape('square')
        self.p1.color('cyan')
        self.p1.shapesize(8,1.8)

        self.p2.shape('square')
        self.p2.color('cyan')
        self.p2.shapesize(8, 1.8)

        self.p1.penup()
        self.p2.penup()

        self.p1.goto(-475,0)
        self.p2.goto(475,0)



        self.ball=turtle.Turtle()
        self.ball.shape("circle")
        self.ball.color("grey")
        self.ball.penup()
        self.ball.shapesize(1.5,1.5)
        self.ball.dx=0.2
        self.ball.dy=0.2
        self.scrn.listen()

        self.scrn.onkeypress(self.p1_up, 'w')
        self.scrn.onkeypress(self.p1_down, 'z')
        self.scrn.onkeypress(self.p2_up, 'i')
        self.scrn.onkeypress(self.p2_down, 'm')

        # score writing

        self.score_a = 0
        self.score_b = 0

        self.pen.showturtle()
        self.pen.color('white')
        self.pen.goto(0, 300)
        self.pen.write("Player A:0          Player B:0", align="center", font=("Courier", 20, "normal"))

        while True:
            self.pen.hideturtle()


            self.scrn.tracer(0)
            #ball movement
            self.ball.goto(self.ball.xcor()+self.ball.dx,self.ball.ycor()+self.ball.dy)


            #ball border collision

            if self.ball.ycor() >= 330 :
                self.ball.sety(330)
                self.ball.dy*=-1
                #winsound.PlaySound("BC.wav",winsound.SND_ASYNC)
            elif self.ball.ycor()<=-330:
                self.ball.sety(-330)
                self.ball.dy *= -1
                #winsound.PlaySound("BC.wav", winsound.SND_ASYNC)

            elif self.ball.xcor()>=480:
                self.ball.setx(480)
                self.ball.dx *= -1
                #winsound.PlaySound("BC.wav", winsound.SND_ASYNC)
            elif self.ball.xcor()<=-480:
                self.ball.setx(-480)
                self.ball.dx *= -1
                #winsound.PlaySound("BC.wav", winsound.SND_ASYNC)

            #ball paddle collision

            if self.ball.xcor()>445 and self.ball.xcor()<475 and self.ball.ycor()<self.p2.ycor()+40 and self.ball.ycor()>self.p2.ycor()-40:
                self.ball.setx(445)
                self.ball.dx *= -1
                self.score_b+=1
                self.pen.clear()
                self.pen.hideturtle()
                self.pen.write("Player A:{}          Player B:{}".format(self.score_a,self.score_b), align="center", font=("Courier", 20, "normal"))
                #winsound.PlaySound("BP.wav", winsound.SND_ASYNC)
            elif self.ball.xcor()<-445 and self.ball.xcor()>-475 and self.ball.ycor()<self.p1.ycor()+40 and self.ball.ycor()>self.p1.ycor()-40:
                self.ball.setx(-445)
                self.ball.dx *= -1
                self.score_a+=1
                self.pen.clear()
                self.pen.hideturtle()
                self.pen.write("Player A:{}         Player B:{}".format(self.score_a,self.score_b), align="center", font=("Courier", 20, "normal"))
                #winsound.PlaySound("BP.wav", winsound.SND_ASYNC)


            # paddles border collision
            elif self.p2.ycor()>260 :
                self.p2.sety(self.p2.ycor()-5)
            elif self.p2.ycor()<-260 :
                self.p2.sety(self.p2.ycor()+5)

            elif self.p1.ycor()>260 :
                self.p1.sety(self.p1.ycor()-5)
            elif self.p1.ycor()<-260 :
                self.p1.sety(self.p1.ycor()+5)

            self.scrn.update()


    # function for paddle movement
    def p1_up(self):
        y = self.p1.ycor()
        y+=20
        self.p1.sety(y)
    def p1_down(self):
        y = self.p1.ycor()
        y-=20
        self.p1.sety(y)
    def p2_up(self):
        y = self.p2.ycor()
        y+=20
        self.p2.sety(y)
    def p2_down(self):
        y = self.p2.ycor()
        y-=20
        self.p2.sety(y)
    '''def playbgm(self):
        winsound.PlaySound("BG.wav", winsound.SND_ASYNC)'''





if __name__=="__main__":
    g = Game()

    turtle.mainloop()
