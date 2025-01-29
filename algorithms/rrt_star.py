import math
import random

from utilities.path import genPath
from utilities.collision import checkCollision
from utilities.kinematics import solveForward


def getRandomJointCoordinate():
  return math.pi * random.random() - math.pi / 2


def getRandomQ():
  return (getRandomJointCoordinate(), getRandomJointCoordinate(), getRandomJointCoordinate())


def norm2(q1, q2):
  return (q1[0] - q2[0]) * (q1[0] - q2[0]) + (q1[1] - q2[1]) * (q1[1] - q2[1]) + (q1[2] - q2[2]) * (q1[2] - q2[2])


def rrtStar(start, end, obstacle, delta=0.05, neighbourhood=2, seed=123):
  random.seed(seed)
  prev = {}
  vertices = []
  vertices.append(start)
  distance = {}
  distance[str(start)] = 0
  found = False
  while not found:
    randomQ = getRandomQ()
    closest = 0
    minDist = 10000
    for i in range(len(vertices)):
      dist = norm2(vertices[i], randomQ)
      if dist < minDist:
        minDist = dist
        closest = i
    dist = math.sqrt(minDist)
    newQ = [0, 0, 0]
    for i in range(3):
      newQ[i] = vertices[closest][i] + \
          (randomQ[i] - vertices[closest][i]) * delta / dist
    newQ = tuple(newQ)
    sol = solveForward(newQ)
    if checkCollision(sol, obstacle):
      continue

    neighbours = []
    minDist = 10000
    for i in range(len(vertices)):
      dist = math.sqrt(norm2(vertices[i], newQ))
      if dist < neighbourhood * delta:
        neighbours.append(i)
        if distance[str(vertices[i])] + dist < minDist:
          minDist = distance[str(vertices[i])] + dist
          closest = i
          neighbours.append(i)

    prev[str(newQ)] = str(vertices[closest])
    vertices.append(newQ)
    distance[str(newQ)] = minDist
    for i in range(len(neighbours)):
      dist = math.sqrt(norm2(vertices[neighbours[i]], newQ))

      if distance[str(newQ)] + dist < distance[str(vertices[neighbours[i]])]:
        distance[str(vertices[neighbours[i]])] = distance[str(newQ)] + dist
        prev[str(vertices[neighbours[i]])] = str(newQ)

    if norm2(newQ, end) <= delta * delta + 0.01:
      prev[str(end)] = str(newQ)
      found = True

  path = genPath(prev, start, end)
  return path, prev
