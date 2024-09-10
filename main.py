import pygame
import random

# Pygame'i başlat
pygame.init()

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ekran boyutu
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Oyun ekranı oluşturma
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')

# FPS ayarı
clock = pygame.time.Clock()
FPS = 60

# Kuş ayarları
BIRD_WIDTH = 50
BIRD_HEIGHT = 35
bird_x = 50
bird_y = SCREEN_HEIGHT // 2
bird_y_velocity = 0
gravity = 0.5
flap_strength = -10

# Boru ayarları
PIPE_WIDTH = 70
PIPE_HEIGHT = random.randint(150, 400)
PIPE_GAP = 150
pipe_x = SCREEN_WIDTH
pipe_speed = 3

# Skor ve font
score = 0
font = pygame.font.Font(None, 36)

# Kuş
