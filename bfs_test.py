import queue
import pygame
from base import *
import time
from collections import deque


def construct_path(parent, current, draw):
    while current in parent:
        current = parent[current]
        current.make_path()
        draw()


def bfs_find_path(draw, grid, start, end):
    begin = time.time()
    Q = deque()
    Q.append(start)
    #Q = queue.Queue(0)
    # Q.put(start)
    open_set_hash = set()
    parent = {}
    while Q:
        print(len(Q))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current = Q.popleft()
        if current not in open_set_hash:
            open_set_hash.add(current)
        # print(len(current.neighbors))
        for neighbor in current.neighbors:
            if neighbor not in open_set_hash:
                Q.append(neighbor)
                open_set_hash.add(neighbor)
                parent[neighbor] = current
                if neighbor == end:
                    construct_path(parent, end, draw)
                    return True
                neighbor.make_open()
        if(current != start):
            current.make_closed()
        print(time.time()-begin)
        draw()
        print(time.time()-begin)
        print(len(open_set_hash))
    return False
