class Frog(object):
    pass


class Bug(object):
    pass


class FrogBug(object):
    pass


class Wizard(object):
    def __init__(self, name):
        self.name = name

    def interact_with(self, obstacle):
        print('{} the Wizard battles against {} and {}!'.format(self, obstacle, obstacle.action()))


class Ork(object):
    @staticmethod
    def action():
        return "kills it!"


class WizardOrk(object):
    def __init__(self, name):
        self.name = name

    def make_character(self):
        return Wizard(self.name)

    @staticmethod
    def make_obstacle():
        return Ork()


class GameEnvironment(object):
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def validate_age(name):
    age = None
    try:
        age = input('Welcome {}. How old are you? '.format(name))
        age = int(age)
    except ValueError:
        print("Age {} is invalid, please try again…".format(age))
        return False, age
    return True, age


def main():
    age = None
    name = input("Hello. what is your name?")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
    game = FrogBug if age < 18 else WizardOrk
    environment = GameEnvironment(game(name))
    environment.play()


if __name__ == '__main__':
    main()
