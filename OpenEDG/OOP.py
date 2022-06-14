class ExampleClass:
    def __init__(self, val = 1):
        self.first = val
    def set_second(self, val):
        self.second = val

example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_2.set_second(3)
example_object_3 = ExampleClass(4)
example_object_3.third = 5

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)

print('-'*100, '\n')

class SuperA:
    var1 = 10
    def funA(self):
        return 11
class SuperB:
    var2 = 20
    def funB(self):
        return 21
class Sub(SuperA, SuperB):
    pass

obj = Sub()

print(obj.var1, obj.funA())
print(obj.var2, obj.funB())

print('-'*100, '\n')
