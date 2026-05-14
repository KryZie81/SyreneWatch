# Importujemy potrzebne biblioteki
import cv2
import numpy

# Ścieżka do pliku wideo
sciezka_do_wideo = "testy/PXL_20241231_230020763.mp4"

# Próg skoku jasności - jeśli różnica między klatkami
# przekroczy tę wartość, oznaczamy to jako zagrożenie
# Analityk ustali docelową wartość - na razie używamy 40
PROG_SKOKU = 40

# Otwieramy plik wideo
wideo = cv2.VideoCapture(sciezka_do_wideo)

# Sprawdzamy czy plik się otworzył
if not wideo.isOpened():
    print("Błąd: Nie można otworzyć pliku wideo!")
else:
    print("Plik wideo otwarty poprawnie!")
    print(f"Próg wykrywania skoku: {PROG_SKOKU}")
    print("-----------------------------------")

# Lista wykrytych zagrożeń
zagrozenia = []

# Zmienna przechowująca jasność poprzedniej klatki
poprzednia_jasnosc = None

# Licznik klatek
licznik = 0

# Pobieramy informację o ilości klatek na sekundę (FPS)
fps = wideo.get(cv2.CAP_PROP_FPS)

# Pętla - pobieramy klatki jedna po drugiej
while True:
    # Pobierz kolejną klatkę
    sukces, klatka = wideo.read()
    
    # Jeśli nie ma więcej klatek - kończymy
    if not sukces:
        break
    
    # Zamieniamy klatkę na szarą
    klatka_szara = cv2.cvtColor(klatka, cv2.COLOR_BGR2GRAY)
    
    # Obliczamy jasność tej klatki
    aktualna_jasnosc = numpy.mean(klatka_szara)
    
    # Porównujemy z poprzednią klatką
    if poprzednia_jasnosc is not None:
        # Obliczamy różnicę jasności
        roznica = abs(aktualna_jasnosc - poprzednia_jasnosc)
        
        # Jeśli różnica przekracza próg - to zagrożenie!
        if roznica > PROG_SKOKU:
            # Obliczamy czas w sekundach
            czas_w_sekundach = licznik / fps
            
            # Zapamiętujemy zagrożenie
            zagrozenia.append({
                "klatka": licznik,
                "czas": czas_w_sekundach,
                "roznica": roznica
            })
    
    # Zapamiętujemy jasność tej klatki na następną iterację
    poprzednia_jasnosc = aktualna_jasnosc
    licznik += 1

# Zamykamy plik wideo
wideo.release()

# Wyświetlamy wyniki
print(f"Przeanalizowano {licznik} klatek")
print(f"Wykryto {len(zagrozenia)} potencjalnych zagrożeń")
print("-----------------------------------")

if len(zagrozenia) == 0:
    print("Brak zagrożeń - wideo jest bezpieczne! ✅")
else:
    print("Lista zagrożeń:")
    for z in zagrozenia:
        minuty = int(z['czas'] // 60)
        sekundy = int(z['czas'] % 60)
        print(f"  ⚠️  Klatka {z['klatka']} | Czas: {minuty}:{sekundy:02d} | Skok jasności: {z['roznica']:.2f}")