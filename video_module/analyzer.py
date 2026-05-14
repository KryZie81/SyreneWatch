# Importujemy potrzebne biblioteki
import cv2
import numpy

def analyze_video(video_path):
    """
    Główna funkcja analizy wideo.
    Przyjmuje ścieżkę do pliku wideo i zwraca wyniki analizy.
    """
    
    # Otwieramy plik wideo
    wideo = cv2.VideoCapture(video_path)
    
    # Sprawdzamy czy plik się otworzył
    if not wideo.isOpened():
        print("Błąd: Nie można otworzyć pliku wideo!")
        return None
    
    # Zmienne do obliczeń
    lista_jasnosci = []
    danger_timestamps = []
    licznik = 0
    poprzednia_jasnosc = None
    PROG_SKOKU = 40
    
    # Pobieramy FPS (klatki na sekundę)
    fps = wideo.get(cv2.CAP_PROP_FPS)
    
    # Pętla - pobieramy klatki jedna po drugiej
    while True:
        sukces, klatka = wideo.read()
        
        # Jeśli nie ma więcej klatek - kończymy
        if not sukces:
            break
        
        # Zamieniamy klatkę na szarą
        klatka_szara = cv2.cvtColor(klatka, cv2.COLOR_BGR2GRAY)
        
        # Obliczamy jasność klatki
        jasnosc = numpy.mean(klatka_szara)
        lista_jasnosci.append(jasnosc)
        
        # Sprawdzamy czy nastąpił skok kontrastu
        if poprzednia_jasnosc is not None:
            roznica = abs(jasnosc - poprzednia_jasnosc)
            if roznica > PROG_SKOKU:
                czas = licznik / fps
                danger_timestamps.append(round(czas, 2))
        
        poprzednia_jasnosc = jasnosc
        licznik += 1
    
    # Zamykamy plik wideo
    wideo.release()
    
    # Zwracamy wyniki w formacie którego potrzebuje kolega
    return {
        "frames": licznik,
        "avg_brightness": round(float(numpy.mean(lista_jasnosci)), 2),
        "max_brightness": round(float(max(lista_jasnosci)), 2),
        "min_brightness": round(float(min(lista_jasnosci)), 2),
        "danger_timestamps": danger_timestamps
    }