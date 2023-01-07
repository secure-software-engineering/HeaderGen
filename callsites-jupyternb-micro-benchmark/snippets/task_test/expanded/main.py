from something import nothing


class Apple:
    def __init__(self):
        pass

    def eat(self):
        pass


class Human:
    def eat_apple(self):
        apple = Apple()
        apple.eat()


human = Human()
human.eat_apple()
nothing(human)
