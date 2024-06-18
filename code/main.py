from settings import *
from level import Level
from pytmx.util_pygame import load_pygame
from os.path import join

class Game:
    def __init__(self):
        pygame.init()

        # Set up the display
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        # Set the window title
        pygame.display.set_caption('Octoman')
        self.clock = pygame.time.Clock()

        # Load the tilemap
        try:
            # Attempt to load the tilemap
            self.tmx_maps = {0: load_pygame(join('..', 'data', 'levels', 'omni.tmx'))}
        except FileNotFoundError:
            print("Could not find the tilemap in the parent directory. Attempting to load from the current directory.")
            self.tmx_maps = {0: load_pygame(join('.', 'data', 'levels', 'omni.tmx'))}

        # Create the level (For Testing Purposes)
        self.current_stage = Level(self.tmx_maps[0])

    def run(self):
        while True:
            # Get the time since the last frame
            dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # Close the window
                    sys.exit() # Close the program

            # Run the level
            self.current_stage.run(dt)
            pygame.display.update()

# If this file is run directly, run the game
if __name__ == '__main__':
    game = Game()
    game.run()