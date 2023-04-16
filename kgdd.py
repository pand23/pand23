import pygame
import random

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dalgona Cookie Game")

# Define the player object
class Player(pygame.sprite.Sprite):
    def init(self):
        super().init()
        self.image = pygame.Surface([50, 50])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

    def update(self):
        # Move the player with the arrow keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

        # Keep the player on the screen
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > screen_width - self.rect.width:
            self.rect.x = screen_width - self.rect.width
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > screen_height - self.rect.height:
            self.rect.y = screen_height - self.rect.height

# Define the cookie object
class Cookie(pygame.sprite.Sprite):
    def init(self):
        super().init()
        self.image = pygame.Surface([30, 30])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

        # Set the initial position of the cookie randomly
        self.rect.x = random.randrange(screen_width - self.rect.width)
        self.rect.y = random.randrange(screen_height - self.rect.height)

    def update(self):
        pass

# Create the sprite groups
all_sprites_group = pygame.sprite.Group()
cookie_group = pygame.sprite.Group()

# Create the player object
player = Player()
all_sprites_group.add(player)

# Create 10 cookie objects
for i in range(10):
    cookie = Cookie()
    all_sprites_group.add(cookie)
    cookie_group.add(cookie)

# Set the initial score to 0
score = 0

# Set the game loop
done = False
clock = pygame.time.Clock()

while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Update the sprites
    all_sprites_group.update()

    # Check for collisions between the player and the cookies
    cookies_collected = pygame.sprite.spritecollide(player, cookie_group, True)
    for cookie in cookies_collected:
        score += 1
        print("Score:", score)

    # Draw the sprites and the score
    screen.fill(BLACK)
    all_sprites_group.draw(screen)
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))

    # Refresh the screen
    pygame.display.flip()

    # Set the game speed
    clock.tick(60)

# Quit Pygame
pygame.quit()