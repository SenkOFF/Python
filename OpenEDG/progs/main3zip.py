#importowanie i dodanie drogi ARCHIWU z projektem do systemowego patchu
from sys import path
path.append('D:\Study\Python\packages\extrapack.zip')

#importowanie modulej.py lub funkcyj z faila modula.py i to wszystko z ZIP'a
import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import FunI
from extra.good.beta import FunB

print(sig.FunS())
print(alp.FunA())
print(FunI())
print(FunB())