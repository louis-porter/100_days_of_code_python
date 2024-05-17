from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Day 20 & 21 - The Snake Game\high_score.txt", "r") as f:
            self.high_score = f.read()
        self.goto(0, 260)
        self.color("white")
        self.hideturtle()
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score : {self.score}, High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.refresh()

    def reset(self):
        if self.score > int(self.high_score):
            with open("Day 20 & 21 - The Snake Game/high_score.txt", "w") as f:
                f.write(str(self.score))  # Convert to string before writing
            self.high_score = str(self.score)  # Update high score attribute
        self.score = 0
        self.refresh()
        

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
        
    
