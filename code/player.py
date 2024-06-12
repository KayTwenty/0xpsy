from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.Surface((48, 56))
        self.image.fill('blue')
        self.rect = self.image.get_frect(topleft = pos)

        # Player movement
        self.direction = vector()
        self.speed = 0.1

    def input(self):
        keys = pygame.key.get_pressed()
        input_vector = vector(0, 0)

        if keys[pygame.K_RIGHT]:
            input_vector.x = 1
        if keys[pygame.K_LEFT]:
            input_vector.x = -1

        # We are normalizing the vector to prevent the player from moving faster diagonally
        # This is caused by the vector having a length of 1.4 instead of 1
        # This is because the vector is a combination of two vectors with a length of 1
        self.direction = input_vector.normalize() if input_vector else input_vector

    def move(self):
        self.rect.topleft += self.direction * self.speed

    def update(self):
        self.input()
        self.move()