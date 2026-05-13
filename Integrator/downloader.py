from yt_dlp import YoutubeDL
import os


def download_video(url):

    # Tworzymy folder temp jeśli nie istnieje
    os.makedirs("temp", exist_ok=True)

    # Konfiguracja yt-dlp
    ydl_opts = {
        "format": "mp4",
        "outtmpl": "temp/video.%(ext)s"
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:

            # Pobieranie filmu
            ydl.download([url])

        # Szukamy pobranego pliku
        for file in os.listdir("temp"):

            if file.endswith(".mp4"):
                return os.path.join("temp", file)

        return None

    except Exception as error:
        print("Błąd podczas pobierania filmu:")
        print(error)

        return None