class Parent:
    def __init__(self):
        print('fatherinit')
    def parentfun(self):
        print('fatherfun')


class Child:
    def __init__(self):
        print('childinit')
    def parentfun(self):
        print('childfun')#子类再写父类算法，覆盖父类算法，在调用子类的前提

c = Child()

c.parentfun()

f = Parent()

f.parentfun()

