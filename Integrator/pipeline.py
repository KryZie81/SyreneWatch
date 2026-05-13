from downloader import download_video

# Import modułu obrazu
from video_module.analyzer import analyze_video

# Import modułu audio
from audio_module.audio_analyzer import analyze_audio

import os
import shutil


def cleanup_temp():

    # Usuwamy folder temp po analizie
    if os.path.exists("temp"):
        shutil.rmtree("temp")


def run_pipeline(url):

    print("Pobieranie filmu...")

    # 1. Pobranie filmu
    video_path = download_video(url)

    if video_path is None:
        print("Nie udało się pobrać filmu")
        return

    print("Film pobrany:")
    print(video_path)

    # 2. Analiza obrazu
    print("Analiza obrazu...")

    video_results = analyze_video(video_path)

    # 3. Analiza audio
    print("Analiza audio...")

    audio_results = analyze_audio(video_path)

    # 4. Łączenie wyników
    final_results = {
        "video_analysis": video_results,
        "audio_analysis": audio_results
    }

    # 5. Czyszczenie plików tymczasowych
    cleanup_temp()

    return final_results


# TEST
if __name__ == "__main__":

    url = "https://www.youtube.com/watch?v=example"

    results = run_pipeline(url)

    print("\nWYNIKI:")
    print(results)