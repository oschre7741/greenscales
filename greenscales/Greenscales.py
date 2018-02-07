#Olivia Schreiner

# Imports
import pygame
import random

# Initialize game engine
pygame.mixer.pre_init()
pygame.init()

#Images
clouds_m = pygame.image.load('images/marimba.png')
rain_m = pygame.image.load('images/marimba_sticks.png')
greenscales = pygame.image.load('images/greenscales.png')
grass = pygame.image.load('images/grass.png')
sun = pygame.image.load('images/sun.png')

# Window
SIZE = (800, 600)
TITLE = "Greenscales And Knuckles"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
GREEN = (0, 175, 0)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)

#Corgi Animation
'''
c1 =
c2 =
c3 =
c4 =
c5 =
c6 =
c7 =
c8 = 
c9 =
c10 =
c11 =
c12 =
'''
# Block
bloc = [380, 280]
vel = [0, 0]
speed = 5

def draw_block(bloc):
    x = bloc[0]
    y = bloc[1]
    
    pygame.draw.rect(screen, WHITE, [x, y, 40, 40])

# Make clouds
num_clouds = 50
clouds = []
for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 200)
    loc = [x, y]
    clouds.append(loc)

def draw_cloud(loc):
    x = loc[0]
    y = loc[1]
    screen.blit(clouds_m, (x, y))

# Make rain
num_rain = 30
rain = []
for i in range(num_rain):
    x = random.randrange(-10, 900)
    y = random.randrange(-600, 0)
    loc = [x, y]
    rain.append(loc)

def draw_rain(loc):
    x = loc[0]
    y = loc[1]
    screen.blit(rain_m, [x,y])

# Sound Effects
click = pygame.mixer.Sound('sounds/click.ogg')
wae = pygame.mixer.Sound('sounds/wae.ogg')

pygame.mixer.music.load('sounds/music.ogg')

daytime = True

# Game loop
pygame.mixer.music.play(-1)

done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                vel[0] = speed
            if event.key == pygame.K_LEFT:
                vel[0] = -1 * speed
            if event.key == pygame.K_UP:
                vel[1] = -1 * speed
            if event.key == pygame.K_DOWN:
                vel[1] = speed
            if event.key == pygame.K_SPACE:
                daytime = not daytime
            elif event.key == pygame.K_c:
                click.play()
            elif event.key == pygame.K_w:
                wae.play()
        elif event.type == pygame.KEYUP:
            vel[0] = 0
            vel[1] = 0
                           
    # Game logic
    bloc[0] += vel[0]
    bloc[1] += vel[1]
    
    for c in clouds:
        c[0] += 2

        if c[0] > 900:
           c[0] = random.randrange(-800, -100)
           c[1] = random.randrange(-50, 200)

    for r in rain:
        r[0] -= 2
        r[1] += 9

        if r[1] > 400 or r[0] < -50:
            r[1] = random.randrange(-600, 0)
            r[0] = random.randrange(-10, 900)

    if daytime:
        sun = pygame.image.load('images/sun.png')
    else:
        pygame.mixer.music.stop()
        sun = pygame.image.load('images/sun1.png')
        clouds_m = pygame.image.load('images/cloud_k.png')
        rain_m = pygame.image.load('images/da_wae.png')
        greenscales = pygame.image.load('images/doyouknowdawae.png')
        grass = pygame.image.load('images/grass1.png')
        
    # Drawing code
    ''' sky '''
    screen.blit(greenscales, (0, 0))

    ''' sun '''
    screen.blit(sun, (600, 0))

    ''' grass '''
    screen.blit(grass, (0, 400))

    ''' rain '''
    for r in rain:
        draw_rain(r)

    ''' clouds '''
    for c in clouds:
        draw_cloud(c)

    ''' block '''
    draw_block(bloc)
        
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
