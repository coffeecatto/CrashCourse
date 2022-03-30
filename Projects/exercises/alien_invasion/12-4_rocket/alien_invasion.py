import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize the game and create resources."""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        # Set the game window's title. 
        pygame.display.set_caption("Alien Invasion")
        
        # Initialize the ship. 
        self.ship = Ship(self)
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events() # Watch for keypresses
            self.ship.update() # Update ship's position on the screen
            self._update_screen() # Update the screen on each frame, I think
    
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_DOWN:
                self.ship.moving_down = True
            elif event.key == pygame.K_UP:
                self.ship.moving_up = True
            elif event.key == pygame.K_q:
                sys.exit()
    
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False
            elif event.key == pygame.K_DOWN:
                self.ship.moving_down = False
            elif event.key == pygame.K_UP:
                self.ship.moving_up = False
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass of the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        # Make the most recently drawn screen visible. 
        pygame.display.flip()

if __name__ == '__main__':
    # Create a game instance and run the game. 
    ai = AlienInvasion()
    ai.run_game()