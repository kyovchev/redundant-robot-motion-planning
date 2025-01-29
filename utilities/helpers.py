def strToTuple(str):
  str2 = str.split(",")
  return (float(str2[0][1:]), float(str2[1]), float(str2[2][:-1]))
