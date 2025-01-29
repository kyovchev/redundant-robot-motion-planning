import cv2

from configs.params import OUTPUT_DIR
from utilities.drawing import drawPath, drawRobot
from utilities.kinematics import solveForward
from utilities.metrics import calculatePathLength


def animatePath(filename, ws, path, fps=15, timeMultiplier=2):
  fourcc = cv2.VideoWriter_fourcc(*'XVID')
  out = cv2.VideoWriter(f'{OUTPUT_DIR}/{filename}.avi', fourcc, fps, (800, 800))

  ws = drawPath(ws, path)

  sol = solveForward(path[0])
  for i in range(fps):
    frame = drawRobot(ws, sol)
    out.write(frame)

  length = calculatePathLength(path)
  time = timeMultiplier * length
  totalFrames = fps * time
  framesPerPoint = int(round(totalFrames / len(path)))

  for i in range(len(path)):
    sol = solveForward(path[i])
    frame = drawRobot(ws, sol)
    for j in range(framesPerPoint):
      out.write(frame)

  sol = solveForward(path[len(path) - 1])
  for i in range(fps):
    frame = drawRobot(ws, sol)
    out.write(frame)
  out.release()
