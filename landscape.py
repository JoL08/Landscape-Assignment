# pygame template
import pygame

pygame.init()

WIDTH = 900
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# -------------------------
# Initialize global variable

sun_radius = 40
sun_growing = 0.2

cloud_x = 100

grass_green = 180
grass_color_change = -1

frames = 0

# -------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # GAME STATE UPDATES
    frames += 1
    cloud_x += 2
    if cloud_x > WIDTH:
        cloud_x = -120
        grass_color_change *= -1

    grass_green += grass_color_change
    if grass_green <= 120 or grass_green >= 200:
        grass_color_change *= -1
    
    sun_radius += sun_growing

    if sun_radius >= 55 or sun_radius <= 35:
         sun_growing *= -1

    # DRAWING
    screen.fill((135, 206, 235))  # sky
    pygame.draw.rect(screen, (70, grass_green, 70), (0, 400, WIDTH, 200))
    pygame.draw.circle(screen, (255, 220, 0), (750, 100), int(sun_radius))
    pygame.draw.polygon(screen, (120, 120, 120), [(50, 400), (180, 180), (310, 400)])
    pygame.draw.polygon(screen, (100, 100, 100), [(220, 400), (380, 140), (540, 400)])
    pygame.draw.polygon(screen, (130, 130, 130), [(450, 400), (620, 200), (790, 400)])
    pygame.draw.ellipse(screen, (70, 140, 255), (250, 430, 400, 100))

    pygame.draw.rect(screen, (200, 150, 100), (600, 300, 180, 130))
    pygame.draw.polygon(screen, (150, 75, 0), [(580, 300), (690, 220), (800, 300)])
    pygame.draw.rect(screen, (100, 60, 20), (670, 360, 40, 70))
    pygame.draw.rect(screen, (180, 230, 255), (625, 330, 35, 35))
    pygame.draw.rect(screen, (180, 230, 255), (720, 330, 35, 35))

    pygame.draw.circle(screen, (255, 255, 255), (cloud_x, 100), 30)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x + 30, 80), 35)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x + 60, 100), 30)
    pygame.draw.ellipse(screen, (255, 255, 255), (cloud_x - 10, 95, 90, 30))

    for x in range(50, 500, 90):
        pygame.draw.rect(screen, (101, 67, 33), (x, 340, 20, 60))
        pygame.draw.circle(screen, (34, 139, 34), (x + 10, 330), 25)
        pygame.draw.circle(screen, (50, 160, 50), (x - 5, 345), 20)
        pygame.draw.circle(screen, (50, 160, 50), (x + 25, 345), 20)

    for x in range(0, WIDTH, 25):
        pygame.draw.rect(screen, (245, 245, 220), (x, 390, 12, 40))
        pygame.draw.polygon(screen, (245, 245, 220), [(x, 390), (x + 6, 380), (x + 12, 390)])

    pygame.draw.rect(screen, (220, 220, 200), (0, 398, WIDTH, 6))
    pygame.draw.rect(screen, (220, 220, 200), (0, 415, WIDTH, 6))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()