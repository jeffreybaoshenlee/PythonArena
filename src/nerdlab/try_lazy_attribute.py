__author__ = "jeffrey"
__date__ = "$2015/6/16 下午 04:17:05$"

class Actor:
    def __init__(self):
        self.hp = 100
        
    def __getattr__(self, name):
        print ('Called __getattr__(%s)' % name)
        if name == 'mp':
            value = 70
            setattr(self, name, value)
            return value

if __name__ == "__main__":
    actor = Actor()
    print(actor.hp)
    print(actor.__dict__)
    print(hasattr(actor,'mp'))
    print(actor.mp)
