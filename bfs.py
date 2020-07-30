import queue
import pygame
from base import *


def construct_path(parent, current, draw):
    while current in parent:
        current = parent[current]
        current.make_path()
        draw()


def bfs_find_path(draw, grid, start, end):
    Q = queue.Queue(0)
    Q.put(start)
    open_set_hash = set()
    parent = {}
    while not Q.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        n = Q.qsize()
        for i in range(n):
            current = Q.get()
            if current == end:
                construct_path(parent, end, draw)
                return True
            open_set_hash.add(current)
            for neighbor in current.neighbors:
                if neighbor not in open_set_hash:
                    Q.put(neighbor)
                    parent[neighbor] = current
                    neighbor.make_open()
            if(current != start):
                current.make_closed()
        draw()
