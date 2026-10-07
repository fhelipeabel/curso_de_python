# Tocando um mp3
# pyrefly: ignore [missing-import]
import pygame
import os

pasta_do_script = os.path.dirname(os.path.abspath(__file__))

caminho_da_musica = os.path.join(pasta_do_script, "ex021.mp3")

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load(caminho_da_musica)
pygame.mixer.music.play()

print("\33[1;33mTocando música... Pressione Ctrl+C no terminal para parar.\33[m")
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)