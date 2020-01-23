
# class Father:
#     fatherpara = 100
#
#     def __init__(self):
#
#         print('调用父类构造函数')
#     def fatherfun1(self):
#         print('调用父类构造函数')
#     def fatherfun2(self, para):
#         Father.fatherpara = para
#         #self.fatherpara = para
#     def getpara(self):
#         print('the para is %d'%self.fatherpara)
#
# #class Child:
#
#
# f = Father()
#
# f.getpara()
# f.fatherfun2(200)
# f.getpara()


class Parent:  # 定义父类
    parentAttr = 100

    def __init__(self):
        print('parentini')

    def parentMethod(self):
        print('调用父类方法')


    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("父类属性 :", Parent.parentAttr)



class Child(Parent):  # 定义子类


    def childMethod(self):
        print('childfun')
        '调用子类方法'


c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()

