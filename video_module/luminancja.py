# Importujemy potrzebne biblioteki
import cv2
import numpy

# Ścieżka do pliku wideo
sciezka_do_wideo = "testy/PXL_20241231_230020763.mp4"

# Otwieramy plik wideo
wideo = cv2.VideoCapture(sciezka_do_wideo)

# Sprawdzamy czy plik się otworzył
if not wideo.isOpened():
    print("Błąd: Nie można otworzyć pliku wideo!")
else:
    print("Plik wideo otwarty poprawnie!")

# Lista która będzie przechowywać jasność każdej klatki
lista_jasnosci = []

# Licznik klatek
licznik = 0

# Pętla - pobieramy klatki jedna po drugiej
while True:
    # Pobierz kolejną klatkę
    sukces, klatka = wideo.read()
    
    # Jeśli nie ma więcej klatek - kończymy
    if not sukces:
        break
    
    # Zamieniamy klatkę z kolorowej na szarą
    # (łatwiej mierzyć jasność na szarej klatce)
    klatka_szara = cv2.cvtColor(klatka, cv2.COLOR_BGR2GRAY)
    
    # Obliczamy średnią jasność klatki przy użyciu NumPy
    jasnosc = numpy.mean(klatka_szara)
    
    # Dodajemy jasność do listy
    lista_jasnosci.append(jasnosc)
    
    licznik += 1

# Zamykamy plik wideo
wideo.release()

# Wyświetlamy wyniki
print(f"Przeanalizowano {licznik} klatek")
print(f"Najmniejsza jasność: {min(lista_jasnosci):.2f}")
print(f"Największa jasność: {max(lista_jasnosci):.2f}")
print(f"Średnia jasność całego wideo: {numpy.mean(lista_jasnosci):.2f}")