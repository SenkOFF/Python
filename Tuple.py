# znalezenie typu
tuple1 = (1, 2, 3)
tuple2 = tuple((1, 2, 3))
print(f"{tuple1} >>> {type(tuple1)}")
print(f"{tuple2} >>> {type(tuple2)}")
print("-"*100, "\n")

# roznica rozmiaru tuple i list
list1 = ['Python', 'is', 'number', 1]
tuple3 = ('Python', 'is', 'number', 1)
print(f"{type(list1)} - {list1} >>> size {list1.__sizeof__()}")
print(f"{type(tuple3)} - {tuple3} >>> size {tuple3.__sizeof__()}")
print("-"*100, "\n")

# przeksztalcenie tuple w list i jego modyfikacja
list2 = list(tuple3) 
print(f"Zmiana tuple - {tuple3} --> w list - {list2} >>> size {list2.__sizeof__()}")
# modyfikacja
list2.append("in the World")
print(f"List - {list2}")
tuple4=tuple(list2)
print(f"Zmiana list - {list2} --> w tuple - {tuple4}")
print("\n")
tuple5 = tuple1 + tuple4
print(tuple5)
print("-"*100, "\n")

# zmiana dannych w list lub dict wewnatrz tuple
tuple6 = ('Python', 'is', 'number', 1, [0, 1, 2], {'user':'Alex'})
print(tuple6)
tuple6[4].append(5)
print(tuple6)
print("-"*100, "\n")