from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Times New Roman', 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        with open("high_score_data.txt") as data:
            self.high_score = int(data.read())
        self.user_score()

    def user_score(self):
        self.goto(0, 270)
        self.color("white")
        self.clear()
        self.write(f"Score: {self.score}  HighScore: {self.high_score}", True, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.user_score()

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("high_score_data.txt", mode="w") as data:
                data.write(str(self.score))
        self.score = 0
        self.user_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("G A M E  O V E R", True, align=ALIGNMENT, font=FONT)
