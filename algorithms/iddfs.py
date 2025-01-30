from collections import deque
import math

from utilities.path import genPath
from utilities.collision import checkCollision
from utilities.kinematics import solveForward


def iddfs(start, end, obstacle, delta=0.05, maxD=100, stepD=100):
  dirs = [(delta,  0.0,    0.0),
          (0.0,  delta,    0.0),
          (0.0,    0.0,  delta),
          (-delta, 0.0,    0.0),
          (0.0, -delta,    0.0),
          (0.0,    0.0, -delta)]
  found = False
  while not found:
    print(maxD)
    curD = 0
    visited = {}
    visited[str(start)] = True
    prev = {}
    stack = deque()
    stack.append((start, curD))
    while stack:
      pos, d = stack.pop()
      if abs(end[0] - pos[0]) < delta + 0.05 and abs(end[1] - pos[1]) < delta + 0.05 and abs(end[2] - pos[2]) < delta + 0.05:
        prev[str(end)] = str(pos)
        found = True
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
        if d < maxD:
          stack.append((next, d + 1))
          visited[str(next)] = True
          prev[str(next)] = str(pos)

    maxD = maxD + stepD

  path = genPath(prev, start, end)
  return path, prev
