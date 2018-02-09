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
refresh_rate = 60

# Colors
GREEN = (0, 175, 0)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)

#Corgi Animation
c1 = pygame.image.load('corgi/corgi.png')
c2 = pygame.image.load('corgi/corgi2.png')
c3 = pygame.image.load('corgi/corgi3.png')
c4 = pygame.image.load('corgi/corgi4.png')
c5 = pygame.image.load('corgi/corgi5.png')
c6 = pygame.image.load('corgi/corgi6.png')
c7 = pygame.image.load('corgi/corgi7.png')
c8 = pygame.image.load('corgi/corgi8.png')
c9 = pygame.image.load('corgi/corgi9.png')
c10 = pygame.image.load('corgi/corgi10.png')
c11 = pygame.image.load('corgi/corgi11.png')
c12 = pygame.image.load('corgi/corgi12.png')

direction = "right"

corgi_right = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12]
corgi_left = []
for c in corgi_right:
    corgi_left.append(pygame.transform.flip(c, True, False))

#Block
bloc = [380, 280]
vel = [0, 0]
speed = 5

def draw_block(bloc):
    x = bloc[0]
    y = bloc[1]

    if direction == "left":
        screen.blit(corgi_left[frame], (x, y))
    elif direction == "right":
        screen.blit(corgi_right[frame], (x, y))   
    
# Make clouds
num_clouds = 30
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
num_rain = 15
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
shut_up = pygame.mixer.Sound("sounds/shutup.ogg")
click = pygame.mixer.Sound('sounds/click.ogg')
wae = pygame.mixer.Sound('sounds/wae.ogg')

pygame.mixer.music.load('sounds/music.ogg')

daytime = True
god = False
god_timer = 0


# Game loop
pygame.mixer.music.play(-1)

done = False

frame = 0
ticks = 0

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = "right"
                vel[0] = speed
            if event.key == pygame.K_LEFT:
                direction = "left"
                vel[0] = -1 * speed
            if event.key == pygame.K_UP:
                vel[1] = -1 * speed
            if event.key == pygame.K_DOWN:
                vel[1] = speed
            if event.key == pygame.K_SPACE:
                daytime = not daytime
            elif event.key == pygame.K_d:
                god = not god
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

    ticks += 1
    if ticks % 5 == 0:
        frame+= 1
        if frame > 11:
            frame = 0
    
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
        clouds_m = pygame.image.load('images/marimba.png')
        rain_m = pygame.image.load('images/marimba_sticks.png')
        greenscales = pygame.image.load('images/greenscales.png')
        grass = pygame.image.load('images/grass.png')
        sun = pygame.image.load('images/sun.png')
    else:
        pygame.mixer.music.stop()
        sun = pygame.image.load('images/sun1.png')
        clouds_m = pygame.image.load('images/cloud_k.png')
        rain_m = pygame.image.load('images/da_wae.png')
        greenscales = pygame.image.load('images/doyouknowdawae.png')
        grass = pygame.image.load('images/grass1.png')


    if god:
        god = pygame.image.load('images/background.png')
    else:
        god = pygame.image.load('images/god.png')
        god_timer = shut_up.play()

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

    ''' god '''
    screen.blit(god, (0, 0))

        
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
