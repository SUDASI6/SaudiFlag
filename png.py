import pygame
import sys

# Initialize Pygame
pygame.init()

# Variables
pixelsize = 1
running = True
delay = 3
color = "#005430"

image = pygame.image.load('./img/imgflag2.png')
width, height = image.get_size()

pygame.display.set_caption('Saudi Flag')
screen = pygame.display.set_mode((width, height))
surf = pygame.Surface((width,height))
screen.fill("#ffffff")
surf.fill("#005430")

# Load the image
# Convert the image for faster pixel access
image = image.convert()

# Main loop
running = True
for x in range(width):
    pygame.draw.rect(screen, color, (x, 0, 4, 4))
    # pygame.time.delay(delay)
    pygame.display.flip()

for y in range(height):
    pygame.draw.rect(screen, color, ((width-4), y, 4, 4))
    pygame.display.flip()

for x in range(width):
    pygame.draw.rect(screen, color, ((width-x), (height-4), 4, 4))
    pygame.display.flip()

for y in range(height):
    pygame.draw.rect(screen, color, (0, (height-y), 4, 4))
    pygame.display.flip()

delay = 100
pixelsize = 1

pygame.time.delay(delay)
screen.fill(color)
pygame.display.flip()


def draw_color(width,height, clr):    
    for x in range(width):
        x = width - x -1
        for y in range(height):
            color = image.get_at((x,y))
            if color == clr:
                pygame.draw.rect(surf,"#ffffff", (x,y, 1,1))

                color = clr
                if image.get_at((x-1,y-1)) != color or image.get_at((x-1, y)) != color or image.get_at((x-1,y+1)) != color or \
                    image.get_at((x,y-1)) != color or image.get_at((x,y+1)) != color or \
                    image.get_at((x+1,y-1)) != color or image.get_at((x+1, y)) != color or image.get_at((x+1,y+1)) != color:
                    pygame.draw.rect(screen,"#ffffff", (x,y, 1,1))
                    pygame.display.flip()
    
    screen.blit(surf,(0,0))
    

draw_color(width,height, (189,72,130))
draw_color(width,height, (102,255,227))
draw_color(width,height, (75,91,171))
draw_color(width,height, (207,255,112))
draw_color(width,height, (235,86,75))
draw_color(width,height, (61,110,112))
draw_color(width,height, (176,48,92))
draw_color(width,height, (87,41,75))
draw_color(width,height, (30,83,228))
draw_color(width,height, (82,12,212))
draw_color(width,height, (180,196,82))
draw_color(width,height, (221,108,33))
draw_color(width,height, (12,28,107))
draw_color(width,height, (96,96,112))
draw_color(width,height, (38,148,152))

# Wait for the user to close
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()