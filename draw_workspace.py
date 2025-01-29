import cv2

from configs.params import *
from utilities.drawing import *


ws, zone00, zone01, zone10, zone11 = drawWorkspace(JOINT_SPACE_DISCRETIZATION)
cv2.imwrite(f'{OUTPUT_DIR}/{FILE_PREFIX}workspace.bmp', ws)
cv2.imwrite(f'{OUTPUT_DIR}/{FILE_PREFIX}workspace_zone00.bmp', zone00)
cv2.imwrite(f'{OUTPUT_DIR}/{FILE_PREFIX}workspace_zone01.bmp', zone01)
cv2.imwrite(f'{OUTPUT_DIR}/{FILE_PREFIX}workspace_zone10.bmp', zone10)
cv2.imwrite(f'{OUTPUT_DIR}/{FILE_PREFIX}workspace_zone11.bmp', zone11)


ws, zone00, zone01, zone10, zone11 = drawWorkspaceWithObstacle(
    OBSTACLE, JOINT_SPACE_DISCRETIZATION)
cv2.imwrite(f'{OUTPUT_DIR}/{FILE_PREFIX}workspace_obstacle.bmp', ws)
cv2.imwrite(f'{OUTPUT_DIR}/{FILE_PREFIX}workspace_obstacle_zone00.bmp', zone00)
cv2.imwrite(f'{OUTPUT_DIR}/{FILE_PREFIX}workspace_obstacle_zone01.bmp', zone01)
cv2.imwrite(f'{OUTPUT_DIR}/{FILE_PREFIX}workspace_obstacle_zone10.bmp', zone10)
cv2.imwrite(f'{OUTPUT_DIR}/{FILE_PREFIX}workspace_obstacle_zone11.bmp', zone11)
