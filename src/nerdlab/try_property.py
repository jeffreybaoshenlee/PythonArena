__author__ = "jeffrey"
__date__ = "$2015/6/11 上午 10:36:20$"

class Actor:
    skill_level = 70
    def __init__(self, hp, mp):
        self._hp = hp
        self._mp = mp

class BoundedActor(Actor):
    def __init__(self, hp, mp):
        super().__init__(hp, mp)
    
    @property
    def hp(self):
        return self._hp
    
    @hp.setter
    def hp(self, hp):
        if hp <= 0:
            raise ValueError('Hp must be bigger than 0. Hp: %d' % hp)
        self._hp = hp

if __name__ == "__main__":
    tom = BoundedActor(10, 50)
    print(tom.hp)
    
    tom.hp = 20
    print(tom.hp)
    print(tom._mp)
    print(tom.skill_level)
    BoundedActor.skill_level += 1
    print(tom.__dict__)
    
    jerry = BoundedActor(100, 500)
    print(jerry.skill_level)
    jerry.skill_level += 2
    print(tom.skill_level)
    print(jerry.skill_level)
    print(jerry.__dict__)
    
    BoundedActor.skill_level += 1
    print(tom.skill_level)
    print(tom.__weakref__)
    print(jerry.skill_level)
    print(jerry.__weakref__)
    
    import pprint
    pprint.pprint(Actor.__dict__)
    pprint.pprint(BoundedActor.__dict__)
    
    print(BoundedActor.hp.__class__.__dict__)
    tom.hp = 0
