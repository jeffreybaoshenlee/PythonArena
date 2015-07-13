__author__ = "jeffrey"
__date__ = "$2015/7/13 下午 01:43:26$"

__all__ = ['Projectile']

class Projectile(object):
    def __init__(self, mass, velocity):
        self.mass = mass
        self.velocity = velocity