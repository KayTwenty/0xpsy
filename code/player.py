from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)

        # Player sprite
        self.image = pygame.Surface((48, 56))
        self.image.fill('blue')

        # Rects
        self.rect = self.image.get_frect(topleft = pos)
        self.old_rect = self.rect.copy()

        # Player movement
        self.direction = vector()
        self.speed = 200

        # Collission detection
        self.collision_sprites = collision_sprites
        

    def input(self):
        keys = pygame.key.get_pressed()
        input_vector = vector(0, 0)

        # Basic check for movement keys being pressed
        # TODO: Swap if statements for switch statements
        if keys[pygame.K_RIGHT]:
            input_vector.x = 1
        if keys[pygame.K_LEFT]:
            input_vector.x = -1

        # We are normalizing the vector to prevent the player from moving faster diagonally
        # This is caused by the vector having a length of 1.4 instead of 1
        # This is because the vector is a combination of two vectors with a length of 1
        self.direction = input_vector.normalize() if input_vector else input_vector

    def move(self, dt):
        self.rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')
        self.rect.y += self.direction.y * self.speed * dt
        self.collision('vertical')

    def collision(self, axis):
        for sprite in self.collision_sprites:
            if self.rect.colliderect(sprite.rect):
                if axis == 'horizontal':
                    # Left position
                    if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                        self.rect.left = sprite.rect.right

                    # Right position
                    if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                        self.rect.right = sprite.rect.left
                else:
                    pass

    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.input()
        self.move(dt)