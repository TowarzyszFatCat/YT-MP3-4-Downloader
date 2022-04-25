import os
from pytube import YouTube
from pathlib import Path

while True:
    podany_link = input("Wklej link do filmu na YouTubie\n")

    if podany_link == "koniec":
        break

    try:
        yt = YouTube(podany_link)

        # Możemy wyświetlić dane o filmie używając:
        print("Tytuł filmu: ", yt.title)
        print("Długość: ", yt.length, " sekund")
        print(f"Wyświetlenia {yt.views}")

        mp3_mp4 = input("Chcesz pobrać mp3 czy mp4? (mp3/mp4)\n")

        if mp3_mp4 == "mp3":
            mp3 = yt.streams.get_audio_only()
            pobrany_mp3 = mp3.download(output_path="./PobraneMP3/")
            print("Pobieranie...")

            # Zamiana z mp4 na mp3
            print("Zmiana z mp4 na mp3...")
            base, ext = os.path.splitext(pobrany_mp3)
            nowy_plik = base + ".mp3"
            os.rename(pobrany_mp3, nowy_plik)
            print("Pobrano!\n")

        elif mp3_mp4 == "mp4":
            print("Pobieranie...")
            mp4 = yt.streams.get_highest_resolution()
            pobrany_mp4 = mp4.download(output_path="./PobraneMP4/")
            print("Pobrano!\n")

        else:
            print("Podałeś złą odpowiedź!\n")
    except:
        print("Podałeś nieprawidłowy link\n")