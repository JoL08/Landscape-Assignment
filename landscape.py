# add sunrise/sunset, add more functions.


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

shadow_x = -100

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)


    # GAME STATE UPDATES
    frames += 1
    cloud_x += 2
    if cloud_x > (WIDTH + 30):
        cloud_x = 0
        shadow_x = -100
        # grass_color_change *= -1

    # grass_green += grass_color_change
    # if grass_green <= 120 or grass_green >= 200:
    #     grass_color_change *= -1
    
    if (cloud_x +60) >= (750 - sun_radius) and (cloud_x - 60) <= (750 + sun_radius):
        shadow_x += 10
    
    sun_radius += sun_growing

    if sun_radius >= 65 or sun_radius <= 35:
         sun_growing *= -1

    # DRAWING
    screen.fill((135, 206, 235))
    pygame.draw.rect(screen, (70, 180, 70), (0, 400, WIDTH, 200))
    pygame.draw.circle(screen, (255, 200, 80), (750, 100), sun_radius)
    pygame.draw.circle(screen, (255, 255, 80), (750, 100), 45)
    pygame.draw.polygon(screen, (120, 120, 120), [(50, 400), (180, 180), (310, 400)])
    pygame.draw.polygon(screen, 'white', [(180, 180), (115, 290), (150, 270), (175, 290), (200, 270), (225, 290), (235, 270)])
    pygame.draw.polygon(screen, (100, 100, 100), [(220, 400), (380, 140), (540, 400)])
    pygame.draw.polygon(screen, (130, 130, 130), [(450, 400), (620, 200), (790, 400)])
    pygame.draw.ellipse(screen, (70, 140, 255), (250, 430, 400, 100))
    pygame.draw.ellipse(screen, (50, 100, 255), (275, 445, 350, 70))
    pygame.draw.ellipse(screen, (30, 70, 255), (300, 460, 300, 40))

# SHADOW
    if (cloud_x) <= 750: 
        pygame.draw.circle(screen, (50, 130, 50), (shadow_x, 500), 100)
        pygame.draw.rect(screen, (50, 130, 50), (0, 400, shadow_x, 300))
        print(cloud_x)
    elif cloud_x >= 750:
        pygame.draw.rect(screen, (50, 130, 50), (450 + (shadow_x - 650), 400, shadow_x, 300))
        pygame.draw.circle(screen, (50, 130, 50), (shadow_x - 100, 500), 100)
    
    
    # CANNOT FIX 2ND PART OF THE SHADOW


# GRADIENT

    pygame.draw.rect(screen, (200, 150, 100), (600, 300, 180, 130))
    pygame.draw.polygon(screen, (150, 75, 0), [(580, 300), (690, 220), (800, 300)])
    pygame.draw.rect(screen, (100, 60, 20), (670, 360, 40, 70))
    pygame.draw.rect(screen, (180, 230, 255), (625, 330, 35, 35))
    pygame.draw.rect(screen, (180, 230, 255), (720, 330, 35, 35))

    pygame.draw.circle(screen, (255, 255, 255), (cloud_x - 30, 100), 30)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x, 80), 35)
    pygame.draw.circle(screen, (255, 255, 255), (cloud_x + 30, 100), 30)
    pygame.draw.ellipse(screen, (255, 255, 255), (cloud_x - 40, 95, 90, 30))

    for x in range(50, 500, 90):
        pygame.draw.rect(screen, (101, 67, 33), (x, 340, 20, 60))
        pygame.draw.circle(screen, (34, 139, 34), (x + 10, 330), 25)
        pygame.draw.circle(screen, (50, 160, 50), (x - 5, 345), 20)
        pygame.draw.circle(screen, (50, 160, 50), (x + 25, 345), 20)

    for x in range(0, WIDTH, 50):
        pygame.draw.rect(screen, (245, 245, 220), (x, 390, 12, 40))
        pygame.draw.polygon(screen, (245, 245, 220), [(x, 390), (x + 6, 370), (x + 12, 390)])

    pygame.draw.rect(screen, (220, 220, 200), (0, 398, WIDTH, 6))
    pygame.draw.rect(screen, (220, 220, 200), (0, 415, WIDTH, 6))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
