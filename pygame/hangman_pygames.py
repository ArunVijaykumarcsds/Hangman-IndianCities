"""
==========================================
  🇮🇳 Hangman Game – Pygame Edition
==========================================

🧠 Description:
A graphical Hangman game built using Pygame. 
It features:
- Mouse-clickable letter buttons
- Lives tracking and visual hangman drawing
- Word guessing logic
- Sound effects for correct/wrong answers

📣 How to Play:
Click letters to guess the hidden word.
Each wrong guess adds to the hangman drawing.
Guess the word before you're out of lives!

🎮 Author: Arun vk
🛠️  Created with: Python & Pygame
📅  Year: 2025
🧑‍💻  Personal project for learning + portfolio

"""

import pygame
import sys
import random
import string
import os

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🇮🇳 Hangman - I ❤ My India")
clock = pygame.time.Clock()

# Absolute path of this script
base_dir = os.path.dirname(os.path.abspath(__file__))
print("Current working directory:", base_dir)
print("Files in directory:", os.listdir(base_dir))  # DEBUG: shows files in folder

# Load sounds with full path
def load_sound(filename):
    path = os.path.join(base_dir, filename)
    if os.path.exists(path):
        try:
            return pygame.mixer.Sound(path)
        except Exception as e:
            print(f"⚠️ Failed to load sound '{filename}':", e)
    else:
        print(f"⚠️ File '{filename}' not found at {path}")
    return None

correct_sound = load_sound("correct.wav")
wrong_sound = load_sound("wrong.wav")

# Fonts and Colors
FONT = pygame.font.SysFont("consolas", 36)
SMALL = pygame.font.SysFont("consolas", 24)
WHITE, BLACK, GRAY, BLUE = (255, 255, 255), (0, 0, 0), (200, 200, 200), (0, 102, 204)

# Game setup
words = """
==========================================
  🇮🇳 Hangman Game – Pygame Edition
==========================================

🧠 Description:
A graphical Hangman game built using Pygame. 
It features:
- Mouse-clickable letter buttons
- Lives tracking and visual hangman drawing
- Word guessing logic
- Sound effects for correct/wrong answers

📣 How to Play:
Click letters to guess the hidden word.
Each wrong guess adds to the hangman drawing.
Guess the word before you're out of lives!

🎮 Author: Arun vk
🛠️  Created with: Python & Pygame
📅  Year: 2025
🧑‍💻  Personal project for learning + portfolio

"""

import pygame
import sys
import random
import string
import os

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🇮🇳 Hangman - I ❤ My India")
clock = pygame.time.Clock()

# Absolute path of this script
base_dir = os.path.dirname(os.path.abspath(__file__))
print("Current working directory:", base_dir)
print("Files in directory:", os.listdir(base_dir))  # DEBUG: shows files in folder

# Load sounds with full path
def load_sound(filename):
    path = os.path.join(base_dir, filename)
    if os.path.exists(path):
        try:
            return pygame.mixer.Sound(path)
        except Exception as e:
            print(f"⚠️ Failed to load sound '{filename}':", e)
    else:
        print(f"⚠️ File '{filename}' not found at {path}")
    return None

correct_sound = load_sound("correct.wav")
wrong_sound = load_sound("wrong.wav")

# Fonts and Colors
FONT = pygame.font.SysFont("consolas", 36)
SMALL = pygame.font.SysFont("consolas", 24)
WHITE, BLACK, GRAY, BLUE = (255, 255, 255), (0, 0, 0), (200, 200, 200), (0, 102, 204)

# Game setup
words = [
    "Delhi", "Mumbai", "Chennai", "Bhopal", "Agra", "Jaipur", "Indore", "Lucknow",
    "Bengaluru", "Hyderabad", "Kolkata", "Pune", "Ahmedabad", "Surat", "Kanpur", "Nagpur",
    "Patna", "Vadodara", "Visakhapatnam", "Ludhiana", "Nashik", "Faridabad", "Meerut", "Rajkot",
    "Varanasi", "Srinagar", "Amritsar", "Ranchi", "Jabalpur", "Gwalior", "Coimbatore", "Madurai",
    "Raipur", "Kota", "Guwahati", "Thiruvananthapuram", "Vijayawada", "Mysuru", "Noida", "Howrah",
    "Aurangabad", "Dhanbad", "Navi Mumbai", "Prayagraj", "Chandigarh", "Shimla", "Dehradun", "Udaipur",
    "Jodhpur", "Panaji"
]

word = random.choice(words).upper()
guessed = set()
lives = 6

# Letter buttons
RADIUS, GAP = 20, 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 450
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(65 + i), True])

def draw_hangman_parts(lives_left):
    pygame.draw.line(screen, BLACK, (150, 500), (450, 500), 5)
    pygame.draw.line(screen, BLACK, (300, 500), (300, 100), 5)
    pygame.draw.line(screen, BLACK, (300, 100), (450, 100), 5)
    pygame.draw.line(screen, BLACK, (450, 100), (450, 150), 5)
    parts = 6 - lives_left
    if parts > 0: pygame.draw.circle(screen, BLACK, (450, 180), 30, 3)
    if parts > 1: pygame.draw.line(screen, BLACK, (450, 210), (450, 300), 3)
    if parts > 2: pygame.draw.line(screen, BLACK, (450, 240), (420, 270), 3)
    if parts > 3: pygame.draw.line(screen, BLACK, (450, 240), (480, 270), 3)
    if parts > 4: pygame.draw.line(screen, BLACK, (450, 300), (420, 350), 3)
    if parts > 5: pygame.draw.line(screen, BLACK, (450, 300), (480, 350), 3)

def draw():
    screen.fill(WHITE)
    draw_hangman_parts(lives)

    display_word = " ".join([l if l in guessed else "_" for l in word])
    text_surface = FONT.render(display_word, True, BLACK)
    screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, 350))

    for x, y, ltr, visible in letters:
        if visible:
            pygame.draw.circle(screen, GRAY, (x, y), RADIUS)
            pygame.draw.circle(screen, BLACK, (x, y), RADIUS, 2)
            txt = SMALL.render(ltr, True, BLACK)
            screen.blit(txt, (x - txt.get_width() // 2, y - txt.get_height() // 2))

    life_text = SMALL.render(f"Lives: {lives}", True, BLACK)
    screen.blit(life_text, (10, 10))

    pygame.display.update()

# Game loop
running = True
while running:
    clock.tick(60)
    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            for btn in letters:
                x, y, ltr, visible = btn
                if visible and (x - mx) ** 2 + (y - my) ** 2 <= RADIUS ** 2:
                    btn[3] = False
                    guessed.add(ltr)
                    if ltr in word:
                        if correct_sound:
                            correct_sound.play()
                    else:
                        lives -= 1
                        if wrong_sound:
                            wrong_sound.play()

    if all(l in guessed for l in word):
        screen.fill(WHITE)
        msg = FONT.render(f"You guessed it! {word}", True, BLUE)
        screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2))
        pygame.display.update()
        pygame.time.delay(3000)
        running = False

    if lives == 0:
        screen.fill(WHITE)
        msg = FONT.render(f"You lost! Word was {word}", True, (200, 0, 0))
        screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2))
        pygame.display.update()
        pygame.time.delay(3000)
        running = False

pygame.quit()
sys.exit()

word = random.choice(words).upper()
guessed = set()
lives = 6

# Letter buttons
RADIUS, GAP = 20, 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 450
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(65 + i), True])

def draw_hangman_parts(lives_left):
    pygame.draw.line(screen, BLACK, (150, 500), (450, 500), 5)
    pygame.draw.line(screen, BLACK, (300, 500), (300, 100), 5)
    pygame.draw.line(screen, BLACK, (300, 100), (450, 100), 5)
    pygame.draw.line(screen, BLACK, (450, 100), (450, 150), 5)
    parts = 6 - lives_left
    if parts > 0: pygame.draw.circle(screen, BLACK, (450, 180), 30, 3)
    if parts > 1: pygame.draw.line(screen, BLACK, (450, 210), (450, 300), 3)
    if parts > 2: pygame.draw.line(screen, BLACK, (450, 240), (420, 270), 3)
    if parts > 3: pygame.draw.line(screen, BLACK, (450, 240), (480, 270), 3)
    if parts > 4: pygame.draw.line(screen, BLACK, (450, 300), (420, 350), 3)
    if parts > 5: pygame.draw.line(screen, BLACK, (450, 300), (480, 350), 3)

def draw():
    screen.fill(WHITE)
    draw_hangman_parts(lives)

    display_word = " ".join([l if l in guessed else "_" for l in word])
    text_surface = FONT.render(display_word, True, BLACK)
    screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, 350))

    for x, y, ltr, visible in letters:
        if visible:
            pygame.draw.circle(screen, GRAY, (x, y), RADIUS)
            pygame.draw.circle(screen, BLACK, (x, y), RADIUS, 2)
            txt = SMALL.render(ltr, True, BLACK)
            screen.blit(txt, (x - txt.get_width() // 2, y - txt.get_height() // 2))

    life_text = SMALL.render(f"Lives: {lives}", True, BLACK)
    screen.blit(life_text, (10, 10))

    pygame.display.update()

# Game loop
running = True
while running:
    clock.tick(60)
    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            for btn in letters:
                x, y, ltr, visible = btn
                if visible and (x - mx) ** 2 + (y - my) ** 2 <= RADIUS ** 2:
                    btn[3] = False
                    guessed.add(ltr)
                    if ltr in word:
                        if correct_sound:
                            correct_sound.play()
                    else:
                        lives -= 1
                        if wrong_sound:
                            wrong_sound.play()

    if all(l in guessed for l in word):
        screen.fill(WHITE)
        msg = FONT.render(f"You guessed it! {word}", True, BLUE)
        screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2))
        pygame.display.update()
        pygame.time.delay(3000)
        running = False

    if lives == 0:
        screen.fill(WHITE)
        msg = FONT.render(f"You lost! Word was {word}", True, (200, 0, 0))
        screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2))
        pygame.display.update()
        pygame.time.delay(3000)
        running = False

pygame.quit()
sys.exit()
