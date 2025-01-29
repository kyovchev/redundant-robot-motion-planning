from collections import deque
import math

from utilities.path import genPath
from utilities.collision import checkCollision
from utilities.kinematics import solveForward


def bfs(start, end, obstacle, delta=0.05):
  dirs = [(delta,  0.0,    0.0),
          (0.0,  delta,    0.0),
          (0.0,    0.0,  delta),
          (-delta, 0.0,    0.0),
          (0.0, -delta,    0.0),
          (0.0,    0.0, -delta)]
  visited = {}
  visited[str(start)] = True
  prev = {}
  stack = deque()
  stack.append(start)
  while stack:
    pos = stack.popleft()
    if abs(end[0] - pos[0]) <= delta and abs(end[1] - pos[1]) <= delta and abs(end[2] - pos[2]) <= delta:
      prev[str(end)] = str(pos)
      break
    for i in range(6):
      next = (pos[0] + dirs[i][0], pos[1] + dirs[i][1], pos[2] + dirs[i][2])
      if str(next) in visited:
        continue
      if next[0] < -math.pi/2 or next[0] > math.pi/2:
        continue
      if next[1] < -math.pi/2 or next[1] > math.pi/2:
        continue
      if next[2] < -math.pi/2 or next[2] > math.pi/2:
        continue
      sol = solveForward(next)
      if checkCollision(sol, obstacle):
        continue
      stack.append(next)
      visited[str(next)] = True
      prev[str(next)] = str(pos)

  path = genPath(prev, start, end)
  return path, prev
