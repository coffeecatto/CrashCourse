import pygame

class Ship:
    """A class to manage the Player's ship."""
    
    def __init__(self, ai_game):
        """Initialize the ship and its starting position."""
        
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load image of the ship and get its rectangles. 
        self.image = pygame.image.load('images/pepeship.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new ship at the bottom center of the screen. 
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)