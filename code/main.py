from settings import *
from level import Level

class Game:
    def __init__(self):
        pygame.init()

        # Set up the display
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        # Set the window title
        pygame.display.set_caption('0xide')

        # Create the level (For Testing Purposes)
        self.current_stage = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # Close the window
                    sys.exit() # Close the program

            # Run the level
            self.current_stage.run()

            # Draw background
            pygame.display.update()

# If this file is run directly, run the game
if __name__ == '__main__':
    game = Game()
    game.run()