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
        self.gravity = 1300
        self.jump = False
        self.jump_height = 900

        # Collission detection
        self.collision_sprites = collision_sprites
        self.on_surface = {'floor': False, 'left': False, 'right': False}
        

    def input(self):
        keys = pygame.key.get_pressed()
        input_vector = vector(0, 0)

        # Basic check for movement keys being pressed
        # TODO: Swap if statements for switch statements
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            input_vector.x = 1
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            input_vector.x = -1

        if keys[pygame.K_SPACE]:
            self.jump = True

        # We are normalizing the vector to prevent the player from moving faster diagonally
        # This is caused by the vector having a length of 1.4 instead of 1
        # This is because the vector is a combination of two vectors with a length of 1
        self.direction.x = input_vector.normalize().x if input_vector else input_vector.x

    def move(self, dt):
        # Horizontal movement
        self.rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')

        # Vertical movement
        self.direction.y += self.gravity / 2 * dt
        self.rect.y += self.direction.y * dt
        self.direction.y += self.gravity / 2 * dt
        self.collision('vertical')

        # Jumping
        if self.jump:
            if self.on_surface['floor']:
                self.direction.y = -self.jump_height
                self.jump = False

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
                    # Top position
                    if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
                        self.rect.top = sprite.rect.bottom

                    # Bottom position
                    if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                        self.rect.bottom = sprite.rect.top
                    
                    # Reset gravity
                    self.direction.y = 0

    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.input()
        self.move(dt)