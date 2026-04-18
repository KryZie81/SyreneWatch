# Importujemy bibliotekę OpenCV - ona umie czytać pliki wideo
import cv2

# Podajemy ścieżkę do naszego pliku wideo
# UWAGA: zmień nazwę pliku na swoją!
sciezka_do_wideo = "testy/PXL_20241231_230020763.mp4"

# Otwieramy plik wideo
wideo = cv2.VideoCapture(sciezka_do_wideo)

# Sprawdzamy czy plik się otworzył poprawnie
if not wideo.isOpened():
    print("Błąd: Nie można otworzyć pliku wideo!")
else:
    print("Plik wideo otwarty poprawnie!")

# Liczymy klatki
licznik_klatek = 0

# Pętla - pobieramy klatki jedna po drugiej
while True:
    # Pobierz kolejną klatkę
    sukces, klatka = wideo.read()
    
    # Jeśli nie ma więcej klatek - kończymy
    if not sukces:
        break
    
    # Zwiększamy licznik
    licznik_klatek += 1

# Zamykamy plik wideo
wideo.release()

# Wyświetlamy wynik
print(f"Pobrano {licznik_klatek} klatek z wideo!")