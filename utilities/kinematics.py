import numpy as np
import math


def solveForward(q):
  a1 = 150
  a2 = 100
  a3 = 100

  q1 = q[0]
  q2 = q[1]
  q3 = q[2]

  s1 = math.sin(q1)
  s2 = math.sin(q2)
  s3 = math.sin(q3)

  c1 = math.cos(q1)
  c2 = math.cos(q2)
  c3 = math.cos(q3)

  R1 = np.array([[c1, -s1, 0],
                 [s1,  c1, 0],
                 [0,    0, 1]])
  R2 = np.array([[c2, -s2, 0],
                 [s2,  c2, 0],
                 [0,    0, 1]])
  R3 = np.array([[c3, -s3, 0],
                 [s3,  c3, 0],
                 [0,    0, 1]])

  Tx1 = np.array([[1, 0, a1],
                  [0, 1,  0],
                  [0, 0,  1]])
  Tx2 = np.array([[1, 0, a2],
                  [0, 1,  0],
                  [0, 0,  1]])
  Tx3 = np.array([[1, 0, a3],
                  [0, 1,  0],
                  [0, 0,  1]])

  M1 = np.matmul(R1, Tx1)
  M2 = np.matmul(np.matmul(M1, R2), Tx2)
  M3 = np.matmul(np.matmul(M2, R3), Tx3)

  p0 = np.array([0, 0])
  p1 = M1[0:2, 2]
  p2 = M2[0:2, 2]
  p3 = M3[0:2, 2]

  return (p0, p1, p2, p3)
