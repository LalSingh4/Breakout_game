import pygame

"""
 This class represents the scoreboard that keeps track of score 
 and lives.
 """
WHITE = (255, 255, 255)

class Scoreboard:
    def __init__(self, font_size):
        self.font = pygame.font.SysFont(None, font_size)
        self.score = 0
        self.lives = 3

    #updating the score
    def update_score(self, points):
        self.score += points

    #reducing the live
    def lose_life(self):
        self.lives -= 1

    #Draws the score and lives
    def draw(self, screen, x, y):
        score_text = self.font.render("Score: " + str(self.score), True, WHITE)
        lives_text = self.font.render("Lives: " + str(self.lives), True, WHITE)
        screen.blit(score_text, (x, y))
        screen.blit(lives_text, (x, y + score_text.get_height() + 5))
