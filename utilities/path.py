from utilities.helpers import strToTuple


def genPath(prev, start, end):
  path = [end]
  cur = str(end)
  while cur in prev:
    cur = prev[cur]
    path = [strToTuple(cur)] + path
  path = [start] + path
  return path
