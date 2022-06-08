import pyAesCrypt
import os

# funkcja szyfrowania plikow
def encrypt(file, password):
    
    #zadajemy rozmiar bufera
    buffer_size = 512*1024

    #wywolujemy metode szyfrowania
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )
    
    #Dla zobaczenia wyniku pokazujemy nazwe pliku
    print("[Plik '" + str(os.path.splitext(file)[0]) + "' szyfrowany]")
    
    #Kasujemy poczatkowy plik
    os.remove(file)
    
#Funkcja skanowania folderu
def walking_by_dirs(dir, password):
    
    #Sprawdzamy wszystkie subfoldery
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        
        #Jesli mamy plik to szyfrujemy
        if os.path.isfile(path):
            try:
                encrypt(path, password)
            except Exception as ex:
                print(ex)
        #Jesli znajdujemy folder, to powtarzamy cykl w wyszukiwaniu plika
        else:
            walking_by_dirs(path, password)
            
password = input('Wprowadz password dla szyfrowania: ')
walking_by_dirs("/d/Study/Python/PyToday/encryptfiles", password)
