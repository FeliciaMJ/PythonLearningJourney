from utils.my_logger import logger

"""
抽象工厂: 是一组用于创建一系列相关事物对象的工厂方法.
抽象工厂设计模式是抽象方法的一种泛化，一个抽象工厂是一组工厂方法，其中的每个工厂方法负责产生不同种类的对象。
好处：让对象的创建容易追踪；将对象的创建与使用解耦；提供优化内存所占用的应用性能的潜力。
     在使用工厂方法时从用户视角通常是看不到的，工厂方法能通过改变激活的工厂方法动态地修改应用行为。
通常一开始使用工厂方法，如果后来发现应用需要更多工厂方法，那么创建一系列对象的过程合并在一起更合理，从而最终引入抽象工厂。

"""

# 我们希望至少包含两个游戏，一个面向孩子，一个面向成人。在运行时，基于用户输入，决定该创建哪个游戏并运行。
# 游戏的创建部分由一个抽象工厂维护。


class Frog(object):
    """
    孩子游戏中的主人公，是一只青蛙。
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        logger().info('{} the Frog encounters {} and {}!'.format(self, obstacle, obstacle.action()))


class Bug(object):
    """
    孩子游戏中的怪兽，是一只虫子。
    """
    def __str__(self):
        return 'a bug'

    @staticmethod
    def action():
        return 'eats it'


class FrogWorld(object):
    """
    是一个抽象工厂，主要职责是创建游戏的主人公和障碍物。区分创建方法并使其名字通用。
    """
    def __init__(self, name):
        self.player_name = name

    def __str__(self):
        return '\n\n\t------ Frog World ------'

    def make_character(self):
        return Frog(self.player_name)

    @staticmethod
    def make_obstacle():
        return Bug()


class Wizard(object):
    """ 成人游戏中的主人公，是一个巫师"""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        logger().info('{} the Wizard battles against {} and {}!'.format(self, obstacle, obstacle.action()))


class Ork(object):
    """ 成人游戏中的怪兽，是怪兽"""
    def __str__(self):
        return 'an evil ork'

    @staticmethod
    def action():
        return 'kills it'


class WizardWorld:
    """ 成人游戏类。"""
    def __init__(self, name):
        self.player_name = name

    def __str__(self):
        return '\n\n\t------ Wizard World ------'

    def make_character(self):
        return Wizard(self.player_name)

    @staticmethod
    def make_obstacle():
        return Ork()


class GameEnvironment(object):
    """ 是游戏的入口，它接受factory作为输入，用其创建游戏的世界。"""
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def validate_age(name):
    age = 0
    try:
        age = input('Welcome {}. How old are you? '.format(name))
        age = int(age)
    except ValueError:
        logger().info("Age {} is invalid, please try again…".format(age))
        return False, age
    return True, age


def main():
    age = 0
    name = input("Hello. What's your name? ")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
    game = FrogWorld if age < 18 else WizardWorld
    environment = GameEnvironment(game(name))
    environment.play()


if __name__ == '__main__':
    main()
