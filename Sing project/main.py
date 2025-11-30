import time
import sys
import pygame

# Inisialisasi pemutar musik
pygame.mixer.init()
pygame.mixer.music.load("Naykilla, Tenxi & Jemsii - Kasih Aba-Aba (Official Music Video) - antinrml.mp3")  # ganti dengan nama file lagumu



# Lirik dengan timestamp (detik, lirik)
lyrics = [
    (109.90, "Aku mau cari jalan tengah"),
    (111.95, "Buat kamu, apa yang nggak bisa?"),
    (114.15, "Ajak kamu ke angkasa"),
    (116.20, "Go to the moon, kita berdansa"),
    (118.33, "Aku wish you best"),
    (120.28, "Kamu yang the best"),
    (122.47, "Kata mamaku"),
    (124.49, '"Masih muda, banyak waktu"')
]


def type_text(text, speed=0.05):
    """Animasi mengetik di terminal"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()  # pindah baris

def main():
    end_timestamp = 127.22
    offset = lyrics[0][0]
    # Mulai putar musik
    pygame.mixer.music.play(start=offset)
    start_time = time.time()

    for ts, line in lyrics:
        # Tunggu sampai waktunya tiba
        while time.time() - start_time < (ts - offset):
            time.sleep(0.01)
        type_text(line, speed=0.075)  # efek mengetik

    # Tunggu musik selesai
    while pygame.mixer.music.get_busy():
        if time.time() - start_time >= (end_timestamp - offset):
            pygame.mixer.music.stop()
            break
        time.sleep(0.1)
   

if __name__ == "__main__":
    main()
