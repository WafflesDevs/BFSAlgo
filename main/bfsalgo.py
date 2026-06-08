import collections
from collections import deque
from queue import PriorityQueue

grid = [
    [0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0]
]

start = (0,0)
goal = (5,5)
current = start
path = dict()
pathway = []
frontier = deque([start])

explored = []

while frontier:

    if(current[1] + 1 < len(grid) and grid[current[0]][current[1]+1] == 0 and (current[0],current[1]+1)  not in explored):
            frontier.append((current[0],current[1]+1))
            path[(current[0],current[1]+1)] = current
    if(current[1] - 1 >= len(grid) and grid[current[0]][current[1]-1] == 0 and (current[0],current[1]-1)  not in explored):
            frontier.append((current[0],current[1]-1))
            path[(current[0],current[1]-1)] = current
    if(current[0] + 1 < len(grid) and grid[current[0]+1][current[1]] == 0 and (current[0]+1,current[1])  not in explored):
            frontier.append((current[0]+1,current[1]))
            path[(current[0]+1,current[1])] = current
    if(current[0] - 1 >= len(grid) and grid[current[0]-1][current[1]] == 0 and (current[0]-1,current[1])  not in explored):
            frontier.append((current[0]-1,current[1]))
            path[(current[0]-1,current[1])] = current

    explored.append(current)
    current = frontier.pop()

    if(current == goal):
           print("goal has been found")
           break

if goal not in path and goal != start:
    print("No goal")
    exit()

cell = goal
while cell != start:
    pathway.append(cell)
    cell = path[cell]

pathway.append(start)
pathway.reverse()

print(pathway)