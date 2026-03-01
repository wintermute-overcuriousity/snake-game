#!/usr/bin/env python3
"""
Snake Game mit Pygame
Steuerung: Pfeiltasten (hoch, runter, links, rechts)
Score: 10 Punkte pro Apfel
Game Over bei Kollision mit Wand oder eigenem Körper
"""

import pygame
import random
import sys

# Initialisierung
pygame.init()

# Fenstergröße
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Farben
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 120, 255)
DARK_GREEN = (0, 180, 0)
GRAY = (50, 50, 50)
YELLOW = (255, 255, 0)

# Spielgeschwindigkeit
FPS = 10

class Snake:
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.length = 3
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([(1, 0), (0, 1), (-1, 0), (0, -1)])
        self.score = 0
        self.grow_pending = 2  # Startlänge von 3
        
    def get_head_position(self):
        return self.positions[0]
    
    def turn(self, point):
        # Verhindere 180-Grad-Drehungen
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        self.direction = point
    
    def move(self):
        head = self.get_head_position()
        x, y = self.direction
        new_x = (head[0] + x) % GRID_WIDTH
        new_y = (head[1] + y) % GRID_HEIGHT
        new_position = (new_x, new_y)
        
        # Kollision mit eigenem Körper
        if new_position in self.positions[1:]:
            return False
            
        self.positions.insert(0, new_position)
        
        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.positions.pop()
            
        return True
    
    def grow(self):
        self.grow_pending += 1
        self.length += 1
        self.score += 10
    
    def draw(self, surface):
        for i, p in enumerate(self.positions):
            # Kopf in anderer Farbe zeichnen
            if i == 0:
                color = BLUE
            else:
                # Farbverlauf für den Körper
                color_intensity = max(100, 255 - (i * 10))
                color = (0, color_intensity, 0)
                
            rect = pygame.Rect(
                p[0] * GRID_SIZE, 
                p[1] * GRID_SIZE, 
                GRID_SIZE, 
                GRID_SIZE
            )
            pygame.draw.rect(surface, color, rect)
            pygame.draw.rect(surface, DARK_GREEN, rect, 1)
            
            # Augen für den Kopf
            if i == 0:
                eye_size = GRID_SIZE // 5
                # Augen basierend auf Richtung positionieren
                if self.direction == (1, 0):  # Rechts
                    left_eye = (rect.right - eye_size - 2, rect.top + eye_size)
                    right_eye = (rect.right - eye_size - 2, rect.bottom - eye_size * 2)
                elif self.direction == (-1, 0):  # Links
                    left_eye = (rect.left + 2, rect.top + eye_size)
                    right_eye = (rect.left + 2, rect.bottom - eye_size * 2)
                elif self.direction == (0, 1):  # Runter
                    left_eye = (rect.left + eye_size, rect.bottom - eye_size - 2)
                    right_eye = (rect.right - eye_size * 2, rect.bottom - eye_size - 2)
                else:  # Hoch
                    left_eye = (rect.left + eye_size, rect.top + 2)
                    right_eye = (rect.right - eye_size * 2, rect.top + 2)
                    
                pygame.draw.circle(surface, WHITE, left_eye, eye_size)
                pygame.draw.circle(surface, WHITE, right_eye, eye_size)
                pygame.draw.circle(surface, BLACK, left_eye, eye_size // 2)
                pygame.draw.circle(surface, BLACK, right_eye, eye_size // 2)

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.randomize_position()
    
    def randomize_position(self):
        self.position = (
            random.randint(0, GRID_WIDTH - 1),
            random.randint(0, GRID_HEIGHT - 1)
        )
    
    def draw(self, surface):
        rect = pygame.Rect(
            self.position[0] * GRID_SIZE,
            self.position[1] * GRID_SIZE,
            GRID_SIZE,
            GRID_SIZE
        )
        # Apfel mit Stiel zeichnen
        pygame.draw.rect(surface, RED, rect)
        pygame.draw.rect(surface, (150, 0, 0), rect, 2)
        
        # Stiel
        stem_rect = pygame.Rect(
            rect.centerx - 2,
            rect.top - 5,
            4,
            8
        )
        pygame.draw.rect(surface, (139, 69, 19), stem_rect)
        
        # Blatt
        leaf_points = [
            (rect.centerx + 2, rect.top - 3),
            (rect.centerx + 8, rect.top - 5),
            (rect.centerx + 6, rect.top)
        ]
        pygame.draw.polygon(surface, GREEN, leaf_points)

def draw_grid(surface):
    for y in range(0, HEIGHT, GRID_SIZE):
        for x in range(0, WIDTH, GRID_SIZE):
            rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(surface, GRAY, rect, 1)

def draw_score(surface, score, font):
    score_text = font.render(f"Score: {score}", True, YELLOW)
    surface.blit(score_text, (10, 10))
    
    length_text = font.render(f"Length: {score // 10 + 3}", True, YELLOW)
    surface.blit(length_text, (10, 40))

def draw_game_over(surface, score, font, big_font):
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(180)
    overlay.fill(BLACK)
    surface.blit(overlay, (0, 0))
    
    game_over_text = big_font.render("GAME OVER", True, RED)
    score_text = font.render(f"Final Score: {score}", True, YELLOW)
    restart_text = font.render("Press SPACE to restart or ESC to quit", True, WHITE)
    
    surface.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 60))
    surface.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
    surface.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 60))

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    
    # Schriftarten
    font = pygame.font.SysFont('Arial', 24)
    big_font = pygame.font.SysFont('Arial', 48, bold=True)
    small_font = pygame.font.SysFont('Arial', 18)
    
    snake = Snake()
    food = Food()
    
    game_over = False
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if game_over:
                    if event.key == pygame.K_SPACE:
                        snake.reset()
                        food.randomize_position()
                        game_over = False
                    elif event.key == pygame.K_ESCAPE:
                        running = False
                else:
                    if event.key == pygame.K_UP:
                        snake.turn((0, -1))
                    elif event.key == pygame.K_DOWN:
                        snake.turn((0, 1))
                    elif event.key == pygame.K_LEFT:
                        snake.turn((-1, 0))
                    elif event.key == pygame.K_RIGHT:
                        snake.turn((1, 0))
        
        if not game_over:
            # Bewegung
            if not snake.move():
                game_over = True
            
            # Essen einsammeln
            if snake.get_head_position() == food.position:
                snake.grow()
                food.randomize_position()
                # Stelle sicher, dass Essen nicht auf der Schlange erscheint
                while food.position in snake.positions:
                    food.randomize_position()
        
        # Zeichnen
        screen.fill(BLACK)
        draw_grid(screen)
        
        # Anleitung
        controls_text = small_font.render("Controls: Arrow Keys | Restart: SPACE | Quit: ESC", True, WHITE)
        screen.blit(controls_text, (WIDTH // 2 - controls_text.get_width() // 2, HEIGHT - 30))
        
        snake.draw(screen)
        food.draw(screen)
        draw_score(screen, snake.score, font)
        
        if game_over:
            draw_game_over(screen, snake.score, font, big_font)
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()