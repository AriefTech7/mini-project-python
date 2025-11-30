import pygame, time

pygame.mixer.init()
pygame.mixer.music.load("Naykilla, Tenxi & Jemsii - Kasih Aba-Aba (Official Music Video) - antinrml.mp3")

pygame.mixer.music.play()
start = time.time()

try:
    while True:
        cmd = input("Tekan [Enter] pas lirik dimulai (atau ketik 'q' buat keluar): ")
        if cmd.lower() == 'q':
            break
        now = time.time() - start
        print(f"Timestamp: {now:.2f} detik")
except KeyboardInterrupt:
    pass
