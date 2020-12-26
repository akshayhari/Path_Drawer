#A small utility program for drawing path
import pygame
from queue import PriorityQueue
pygame.init()
###########################
# Change your properties here - block_size should be divisible by screen_size
# Don't remove 'r' in the path
screen_size = 600   # Window size
block_size = 10     # Size of each block
image_loc = r"C:\Users\aksha\Pictures\sample.jpg"  # Location  of background image - 
file_loc = r"C:\Users\aksha\Pictures\list.txt"     # Location where output should be stored
barrier = 'B'   # Default character for the obstacle
road = ''       # Character for path
#############################
#############################
screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption('Path Drawer')
background = pygame.image.load(image_loc)
screen.blit(background,(0,0))
#Making square grids of equal sizes
def make_grid(screen_size, block_size):
    grid = []
    row = screen_size // block_size
    for i in range(row):
        grid.append([])
        for j in range(row):
            grid[i].append(barrier)
    return grid

#Mapping window position to grid position
def get_grid_pos(pos, screen_size, block_size):
    x,y = pos
    row = y // block_size
    col = x // block_size
    return row,col
    
#Color Tuples
WHITE = (255, 255, 255) 
RED = (255, 0 , 0) 
#Drawing the matrix grid
def draw(screen, grid, screen_size, block_size):
    background = pygame.image.load(image_loc)
    screen.blit(background,(0,0))
    for i in range(0, screen_size, block_size):
        for j in range(0, screen_size, block_size):
            row = i//block_size
            col = j//block_size
            if grid[row][col] == road:
                pygame.draw.rect(screen, RED, pygame.Rect(j, i, block_size, block_size))

# Main function        
def main():
    grid = make_grid(screen_size,block_size)
    running = True
    while running:
        #Various events that may happen
        for event in pygame.event.get():
            #For Exiting Window
            if event.type == pygame.QUIT:
                running = False
            # Escape key for reseting the 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    grid = make_grid(screen_size,block_size)
                    pygame.display.flip()
                    continue
            #Left Click for adding start,end and obstacles
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row,col=get_grid_pos(pos,screen_size,block_size)
                if grid[row][col] == barrier:
                    grid[row][col] = road
            #Right click for deleting cell
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row,col = get_grid_pos(pos,screen_size,block_size)
                if grid[row][col] != barrier:
                    grid[row][col] = barrier
        draw(screen,grid,screen_size,block_size)
        pygame.display.update()
# Output file  - Make changes here how you want your file
    op = open(file_loc, 'w')
    for row in grid:
        op.write(str(row) + '\n')
    op.close()
main()
