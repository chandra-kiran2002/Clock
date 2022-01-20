from turtle import Turtle


class Digital_clock(Turtle):
    def __init__(self):
        super().__init__()
        self.seconds = 0
        self.minutes = 0
        self.hours = 12

    def set_time(self, x):
        self.seconds = x[2]
        self.minutes = x[1]
        self.hours = x[0]

    def change_time(self, t):
        if t == 60 and self.minutes == 59 and self.hours == 12:
            self.hours = 1
        elif t == 60 and self.minutes == 59:
            self.hours += 1
        if t == 60 and self.minutes != 59:
            self.minutes += 1
        elif self.minutes == 59 and t == 60:
            self.minutes = 0
        if t == 60:
            self.seconds = 0
        else:
            self.seconds = t

        self.clear()
        self.write(f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}', align="center",
                   font=("Arial", 15, "normal"))
