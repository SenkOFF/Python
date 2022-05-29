# importowanie bazy
import keyword

print(keyword.kwlist)

# zrobienie listy w pionie
for kw in keyword.kwlist:
    print(kw)
    print(id(kw))