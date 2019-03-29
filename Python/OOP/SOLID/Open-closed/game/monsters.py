from Character import Monster

# from abc import abstractmethod, ABCMeta

# def MonsterFactory(kind):
#     if kind == 'Fire':
#         return FireMonster(kind)
#     elif kind == 'Ice':
#         return IceMonster(kind)
#     elif kind == 'Stone':
#         return StoneMonster(kind)
#     elif kind == 'Kungfu':
#         return KungfuMonster(kind)


# 게임 개발 초기의 몬스터 종류는 두 가지
class FireMonster(Monster):
    def generate_gold(self):
        return 10

class IceMonster(Monster):
    def __init__(self):
        super().__init__()
        self.hp = 100

    def generate_gold(self):
        return 20

# 게임 규모가 커지면서 추가된 몬스터 
class StoneMonster(Monster):
    def generate_gold(self):
        return 0

class KungfuMonster(Monster):
    def generate_gold(self):
        return 1000

class ArrowMonster(Monster):
    def generate_gold(self):
        return 500