class Apple:
    def __init__(self):
        pass

    def eat(self):
        pass


class Human:
    @staticmethod
    def eat_apple():
        apple = Apple()
        apple.eat()


human = Human()
human.eat_apple()
