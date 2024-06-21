class Turtle(object):

    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.x

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s - 1 <= 0:
            print("Ошибка размерности черепашки")
        else:
            self.s -= 1

    def count_moves(self):
        count = 0
        final_x, final_y = 2, 2
        if self.x > final_x: # идем влево
            while self.x > final_x:
                self.go_left()
                count += 1
        elif self.x < final_x: # идем вправо
            while self.x < final_x:
                self.go_right()
                count += 1
        if self.y > final_y: # идем вниз
            while self.y > final_y:
                self.go_down()
                count += 1
        elif self.y < final_y: # идем вверх
            while self.y < final_y:
                self.go_up()
                count += 1
        return count

turtle = Turtle(10, 10, 5)
print(turtle.count_moves())
turtle.degrade()
turtle.degrade()
turtle.degrade()
turtle.degrade()
turtle.degrade()