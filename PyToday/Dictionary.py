# znalezenie typu
dict1 = {}
dict2 = dict()
print(type(dict1))
print(type(dict2))

# stworzenie biblioteki
dict3 = {
    "food":["apple", "orange", "banana", "peanuts"],
    "user":"Pol",
    "surname":"Hrust",
    "age": 32,
    "tuples":(1, 2, 3)
    }
print(dict3) # cala biblioteka
print(dict3["surname"]) # odpowiednie znaczenie
print("-"*100)

# dodanie znaczenia do biblioteki
dict3 ["weight"]=100
dict3 [7]="July"
print(dict3)

# zmiana wybranego znaczenia (a nie klucz)
dict3 ["weight"]=90
print(dict3)

# skasowanie znaczenia
del dict3["tuples"]
print(dict3)
print("-"*100)

# sprawdzenie calej biblioteki i wynik w pionie
for k, v in dict3.items():
    print(f"{k} >>> {v}")
print("-"*100)

# wynik tylko klucze(standartowo)                 rowniez 
for key in dict3:                   #   for key in dict3.keys():
    print(key)                      #       print(key)
print("<>"*5)
# wynik tylko znaczenie
for value in dict3.values():
    print(value)
print("-"*100)
    
# pokazac list z biblioteki
for v in dict3["food"]:
    print(v)
print("-"*100)
    
# biblioteki w bibliotece
dict4 = {
    "Pawel" : {
        "food":["apple", "orange", "banana", "peanuts"],
        "user":"Pol",
        "surname":"Hrust",
        "age": 32,
    },
    "Nesci" : {
        "food":["mango", "orange", "avakado", "grejpfrut"],
        "user":"Nes",
        "surname":"War",
        "age": 30,
    }
}
for k, v in dict4.items():
    print(f"{k} >>> {v}")
print("-"*100)
    
# uzyskanie dokladnego znaczenie z wewnetznej biblioteki
for name, info in dict4.items():
    print(f"Uzytkownik: {name}")
# wprowadzienie variables   
    nazw=info["surname"]
    wek=info['age']
    food=info["food"]
# pokazanie dokladnego    
    print(f"Nazwisko {name} - {nazw}")
    print(f"Twoj wiek {name} - {wek}")
    print(f"Ulubione owoce {name} - {food}\n")