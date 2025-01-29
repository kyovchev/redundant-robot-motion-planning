import cv2
import time

from algorithms.rrt_star import rrtStar
from configs.params import *
from utilities.animate import animatePath
from utilities.drawing import drawObstacle, drawPathWithRobot, drawWorkspaceTree
from utilities.metrics import getAllMetrics


ws = cv2.imread(f'{OUTPUT_DIR}/{FILE_PREFIX}workspace_obstacle.bmp')

startTime = time.time()
path, prev = rrtStar(START, END, OBSTACLE, delta=DELTA)
time = time.time() - startTime

ws = drawObstacle(ws, OBSTACLE)
wsPath = drawPathWithRobot(ws, path)

cv2.imwrite(f'{OUTPUT_DIR}/{FILE_PREFIX}rrt_star_{DELTA}.bmp', wsPath)

ws2 = drawWorkspaceTree(ws, prev)
cv2.imwrite(f'{OUTPUT_DIR}/{FILE_PREFIX}rrt_star_{DELTA}_tree.bmp', ws2)

animatePath(f'{FILE_PREFIX}rrt_star_{DELTA}', ws, path, 10)

getAllMetrics(f'{FILE_PREFIX}rrt_star_{DELTA}', path, prev, time)
