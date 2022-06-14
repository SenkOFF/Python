class Color:
    red = 0
    green = 0
    blue = 0
    def __init__(self, r, g, b):
        red = r
        green = g
        blue = b
    def toHex(self):
        return '#%02x%02x%02x' % (red, green, blue)

class ColorAlpha(Color):
    alpha = 1
    def __init__(self, r, g, b, a):
        red = r
        green = g
        blue = b
        alpha = a
    
gray = Color(80, 80, 80) #Szary kolor
red = ColorAlpha(255, 0, 0, .5) #Na pol przezroszyczty
print(gray, '\n', red)
print('-'*100, '\n')



class SomeClass(object):
    attr1 = 42
    def method1(self, x):
        return 2*x
obj = SomeClass()
print(obj.method1(6)) # 12
print(obj.attr1) # 42
print('-'*100, '\n')



class Point(object):
    def __init__(self, x, y, z):
        self.coord = (x, y, z)
p = Point(13, 14, 15)
print(p.coord) # (13, 14, 15)