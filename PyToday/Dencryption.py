import pyAesCrypt
import os

# funkcja rozszefrowania plikow
def decryption(file, password):
    
    #zadajemy rozmiar bufera
    buffer_size = 512*1024

    #wywolujemy metode rozszefrowania
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
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
        
        #Jezeli mamy plik to rozszefrujemy
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        #Jesli znajdujemy folder, to powtarzamy cykl w wyszukiwaniu plika
        else:
            walking_by_dirs(path, password)
            
password = input('Wprowadz password dla rozszefrowania: ')
walking_by_dirs('/d/Study/Python/PyToday/encryptfiles', password)
