class Horse:

    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'
        self.dx = 0

    def run(self, dx):
        self.dx = dx
        self.x_distance += self.dx


class Eagle:

    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'
        self.dy = 0

    def fly(self, dy):
        self.dy = dy
        self.y_distance += self.dy


class Pegasus(Eagle, Horse):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
