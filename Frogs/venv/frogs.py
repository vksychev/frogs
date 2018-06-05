class Lamp:
    def __init__(self, number):
        self._shine = False
        self.number = number

    def __str__(self):
        return '{} : {}'.format(self.number, self._shine)

    def switch(self):
        self._shine = not self._shine


class Frog:
    def __init__(self, number):
        self.number = number
        self.pos = 0

    def jump(self):
        self.pos += self.number
        return self.pos


if __name__ == "__main__":

    frogs = []
    for i in range(100):
        n = i + 1
        frogs.append(Frog(n))

    lamps = []
    for i in range(100):
        n = i + 1
        lamps.append(Lamp(n))


    # press(i)
    def press(i):
        lamps[i - 1].switch()


    for i in range(100):
        r = frogs[i].jump()
        while r <= 100:
            press(r)
            r = frogs[i].jump()
