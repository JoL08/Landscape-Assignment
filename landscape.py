# add sunrise/sunset, add more functions.


# pygame template
import pygame
import math

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

sun_x = 150
sun_y = 600
moon_radius = 60
moon_x = 750
moon_y = 600

cloud_x = 100

shadow_x = -100

sunrise = (230, 150, 80)
midday  = (135, 206, 235)

speed = 0.005
acceleration = 0.00001

frames = 0

# -------------------------

def draw_sun(x, y, sun_radius):
    pygame.draw.circle(screen, (255, 200, 80), (x, y), sun_radius)
    pygame.draw.circle(screen, (255, 255, 80), (x, y), 45)

def draw_moon(x, y, moon_radius):
    pygame.draw.circle(screen, (200, 200, 200), (x, y), moon_radius)
    pygame.draw.circle(screen, (220, 220, 220), (x, y), moon_radius - 5)
    pygame.draw.circle(screen, (135, 206, 235), (x + 15, y - 10), moon_radius - 10)

def draw_mountain():
    pygame.draw.polygon(screen, (120, 120, 120), [(50, 400), (180, 180), (310, 400)])
    pygame.draw.polygon(screen, 'white', [(180, 180), (115, 290), (150, 270), (175, 290), (200, 270), (225, 290), (235, 270)])
    pygame.draw.polygon(screen, (100, 100, 100), [(220, 400), (380, 140), (540, 400)])
    pygame.draw.polygon(screen, 'white', [(380, 140), (300, 270), (350, 230), (380, 250), (410, 240), (460, 270)])
    pygame.draw.polygon(screen, (130, 130, 130), [(450, 400), (620, 200), (790, 400)])
    pygame.draw.polygon(screen, 'white', [(620, 200), (535, 300), (580, 280), (610, 300), (640, 280), (670, 300), (705, 280)])

def sunrise():
    t = (math.sin(frames * 0.005) + 1) / 2
    R1 = int(250 + (135 - 250) * t)
    G1 = int(176 + (206 - 176) * t)
    B1 = int(40  + (235 - 40)  * t)
    screen.fill((R1, G1, B1))

def sunset():
    t = (math.sin(frames * 0.005) + 1) / 2
    R2 = int(135 + (2   - 135) * t)
    G2 = int(206 + (117 - 206) * t)
    B2 = int(235 + (156 - 235) * t)
    screen.fill((R2, G2, B2))

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # GAME STATE UPDATES
    frames += 1
    cloud_x += 2
    if cloud_x > (WIDTH + 30):
        cloud_x = 0
        shadow_x = -100
        
    sun_radius += sun_growing

    if sun_radius >= 65 or sun_radius <= 35:
         sun_growing *= -1

    # DRAWING
    if sun_y < 400 and sun_x < 450:
        sunrise()
    elif sun_y < 400 and sun_x > 450:
        sunset()

    # sun and moon
    sun_x = -math.cos(frames * speed) * 500 + 450
    sun_y = -math.sin(frames * speed) * 300 + 400
    draw_sun(sun_x, sun_y, sun_radius)
    moon_x = 920 - sun_x
    moon_y = 800 - sun_y
    draw_moon(moon_x, moon_y, moon_radius)
    print(sun_x, sun_y)
    
    # grass
    pygame.draw.rect(screen, (70, 180, 70), (0, 400, WIDTH, 200))

    # mountains
    draw_mountain()

    # pond
    pygame.draw.ellipse(screen, (70, 140, 255), (250, 430, 400, 100))
    pygame.draw.ellipse(screen, (50, 100, 255), (275, 445, 350, 70))
    pygame.draw.ellipse(screen, (30, 70, 255), (300, 460, 300, 40))

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
