from shapely.geometry import LineString, Point


def checkCollision(sol, obstacle):
  p = Point(obstacle[0], obstacle[1])
  c = p.buffer(obstacle[2]).boundary
  for i in range(3):
    l = LineString([(int(sol[i][0]), int(sol[i][1])),
                    (int(sol[i + 1][0]), int(sol[i + 1][1]))])
    if c.intersects(l):
      return True
  return False
