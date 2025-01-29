from configs.params import *


def calculatePathLength(path):
  total = 0
  for i in range(1, len(path)):
    total = total + max(abs(path[i - 1][0] - path[i][0]), max(
        abs(path[i - 1][1] - path[i][1]), abs(path[i - 1][2] - path[i][2])))
  return total


def getAllMetrics(filename, path, prev, time):
  print(f'Time: {time:.2f} s')
  print(f'Explored nodes: {len(prev)}')
  print(f'Path nodes: {len(path)}')
  print(f'Path length: {calculatePathLength(path):.2f}')
  print(f'Start: {START}')
  print(f'End: {END}')
  print(f'Obstacle: {OBSTACLE}')

  with open(f'{OUTPUT_DIR}/{filename}.txt', 'w') as f:
    f.write(f'Time: {time:.2f} s\n')
    f.write(f'Explored nodes: {len(prev)}\n')
    f.write(f'Path nodes: {len(path)}\n')
    f.write(f'Path length: {calculatePathLength(path):.2f}\n')
    f.write(f'Start: {START}\n')
    f.write(f'End: {END}\n')
    f.write(f'Obstacle: {OBSTACLE}\n')
