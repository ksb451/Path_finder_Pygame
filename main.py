import pygame
import math
from base import *
from Astar import *
from bfs import *

WIDTH = 600  # Width of the Application Screen
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Path Finding Visuaizer")


# return the cell clicked by using width of screen and cordinates and no of ros
def get_clicked_pos(pos, rows, width):
    gap = width//rows
    y, x = pos

    row = y//gap
    col = x//gap
    return row, col

# main application loop


def main(win, width):
    ROWS = 50  # size of grid
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    started = False
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.mouse.get_pressed()[0]:  # left-click
                pos = pygame.mouse.get_pos()  # returns a tuplewith x and y cordinate of screen
                # get the row and column index
                row, col = get_clicked_pos(pos, ROWS, WIDTH)
                spot = grid[row][col]
                if not start:
                    start = spot
                    start.make_start()
                elif not end:
                    end = spot
                    end.make_end()
                elif spot != end and spot != start:
                    spot.make_barrier()
            elif pygame.mouse.get_pressed()[2]:  # right-click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                if spot == end:
                    end = None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and start and end and not started:  # A*
                    started = True
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)

                    algorithm(lambda: draw(win, grid, ROWS, width),
                              grid, start, end)
                if event.key == pygame.K_b and start and end and not started:  # BFS
                    started = True
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)
                    bfs_find_path(lambda: draw(
                        win, grid, ROWS, width), grid, start, end)
                if event.key == pygame.K_r:  # reset
                    started = False
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)

    pygame.quit()


main(WIN, WIDTH)
