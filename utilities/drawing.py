import math
import numpy as np
import cv2

from utilities.helpers import strToTuple

from .collision import checkCollision
from .kinematics import solveForward

WORKSPACE_COLOR = [192, 192, 192]
PATH_COLOR = [34, 139, 34]
OBSTACLE_COLOR = [192, 0, 0]
ROBOT_COLOR = [65, 22, 160]
TREE_VERTEX_COLOR = [0, 0, 0]
# TREE_EDGE_COLOR = [200, 213, 48]
TREE_EDGE_COLOR = [65, 22, 160]

CX = 400
CY = 400


def drawWorkspace(count=50):
  ws = 255 * np.ones((2 * CX, 2 * CY, 3), np.uint8)
  zone00 = 255 * np.ones((2 * CX, 2 * CY, 3), np.uint8)
  zone01 = 255 * np.ones((2 * CX, 2 * CY, 3), np.uint8)
  zone10 = 255 * np.ones((2 * CX, 2 * CY, 3), np.uint8)
  zone11 = 255 * np.ones((2 * CX, 2 * CY, 3), np.uint8)
  for q1 in np.linspace(-math.pi/2, math.pi/2, count):
    for q2 in np.linspace(-math.pi/2, math.pi/2, count):
      for q3 in np.linspace(-math.pi/2, math.pi/2, count):
        sol = solveForward((q1, q2, q3))
        px = int(CX + round(sol[3][0]))
        py = int(CY - round(sol[3][1]))
        ws[py, px] = WORKSPACE_COLOR
        if q2 <= 0 and q3 <= 0:
          zone00[py, px] = WORKSPACE_COLOR
        if q2 <= 0 and q3 >= 0:
          zone01[py, px] = WORKSPACE_COLOR
        if q2 >= 0 and q3 <= 0:
          zone10[py, px] = WORKSPACE_COLOR
        if q2 >= 0 and q3 >= 0:
          zone11[py, px] = WORKSPACE_COLOR

  return ws, zone00, zone01, zone10, zone11


def drawWorkspaceWithObstacle(obstacle, count=50):
  ws = 255 * np.ones((2 * CX, 2 * CY, 3), np.uint8)
  zone00 = 255 * np.ones((2 * CX, 2 * CY, 3), np.uint8)
  zone01 = 255 * np.ones((2 * CX, 2 * CY, 3), np.uint8)
  zone10 = 255 * np.ones((2 * CX, 2 * CY, 3), np.uint8)
  zone11 = 255 * np.ones((2 * CX, 2 * CY, 3), np.uint8)
  for q1 in np.linspace(-math.pi/2, math.pi/2, count):
    for q2 in np.linspace(-math.pi/2, math.pi/2, count):
      for q3 in np.linspace(-math.pi/2, math.pi/2, count):
        sol = solveForward((q1, q2, q3))
        if checkCollision(sol, obstacle):
          continue
        px = int(CX + round(sol[3][0]))
        py = int(CY - round(sol[3][1]))
        cv2.circle(ws, (px, py), 1, tuple(WORKSPACE_COLOR), -1)
        if q2 <= 0 and q3 <= 0:
          cv2.circle(zone00, (px, py), 1, tuple(WORKSPACE_COLOR), -1)
        if q2 <= 0 and q3 >= 0:
          cv2.circle(zone01, (px, py), 1, tuple(WORKSPACE_COLOR), -1)
        if q2 >= 0 and q3 <= 0:
          cv2.circle(zone10, (px, py), 1, tuple(WORKSPACE_COLOR), -1)
        if q2 >= 0 and q3 >= 0:
          cv2.circle(zone11, (px, py), 1, tuple(WORKSPACE_COLOR), -1)

  return ws, zone00, zone01, zone10, zone11


def drawRobot(ws, sol):
  ws = ws.copy()
  for i in range(3):
    cv2.line(ws, (CX + int(sol[i][0]), CY - int(sol[i][1])),
             (CX + int(sol[i + 1][0]), CY - int(sol[i + 1][1])), tuple(ROBOT_COLOR), 3)
    for i in range(3):
      cv2.circle(ws, (CX + int(sol[i][0]), CY -
                 int(sol[i][1])), 5, tuple(ROBOT_COLOR), -1)

  return ws


def drawObstacle(ws, obstacle):
  ws = ws.copy()
  cv2.circle(
      ws, (CX + int(obstacle[0]), CY - int(obstacle[1])), int(obstacle[2]) - 2, tuple(OBSTACLE_COLOR), -1)

  return ws


def drawPath(ws, path):
  ws = ws.copy()
  for i in range(len(path) - 1):
    sol1 = solveForward(path[i])
    sol2 = solveForward(path[i + 1])
    cv2.line(ws, (CX + int(sol1[3][0]), CY - int(sol1[3][1])),
             (CX + int(sol2[3][0]), CY - int(sol2[3][1])), tuple(PATH_COLOR), 3)

  return ws


def drawPathWithRobot(ws, path, delta=0.8):
  ws = ws.copy()
  prevQ = path[0]
  ws = drawRobot(ws, solveForward(path[0]))
  for i in range(1, len(path) - 1):
    sol = solveForward(path[i])
    if abs(path[i][0] - prevQ[0]) >= delta or \
       abs(path[i][1] - prevQ[1]) >= delta or \
       abs(path[i][2] - prevQ[2]) >= delta:
      prevQ = path[i]
      sol = solveForward(path[i])
      ws = drawRobot(ws, sol)
  soln = solveForward(path[len(path) - 1])
  ws = drawRobot(ws, soln)
  ws = drawPath(ws, path)

  return ws


def drawWorkspaceTree(ws, prev):
  ws = ws.copy()

  for u, v in prev.items():
    sol1 = solveForward(strToTuple(u))
    sol2 = solveForward(strToTuple(v))
    cv2.line(ws, (CX + int(sol1[3][0]), CY - int(sol1[3][1])),
             (CX + int(sol2[3][0]), CY - int(sol2[3][1])), tuple(TREE_EDGE_COLOR), 1)
    cv2.circle(ws, (CX + int(sol1[3][0]), CY -
               int(sol1[3][1])), 2, tuple(TREE_VERTEX_COLOR), -1)
    cv2.circle(ws, (CX + int(sol2[3][0]), CY -
               int(sol2[3][1])), 2, tuple(TREE_VERTEX_COLOR), -1)

  return ws
