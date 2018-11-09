inval = 312051

dirs = ['r', 'u', 'l', 'd']
vectordirs = {'r':1, 'u':1, 'l':-1, 'd':-1}
horizontals = ['r', 'l']
verticals = ['u', 'd']

def nextdir(dir):
  """Moves direction to the next one anticlockwise"""
  return dirs[(dirs.index(dir) + 1) % 4]


def getcoordinates(x):
  """Gets coordinates of x in a spiral starting at 1 and moving outwards""" 
  coords = [0, 0] #up, right positive; down, left negative
  i = 1
  step = 1  #number of steps in spiral
  dir ='r' #direction currently moving
  while i < x:

    for y in range(step):

      if i >= x:
        continue
      if dir in horizontals:
        coords[0] += vectordirs[dir]
      if dir in verticals:
        coords[1] += vectordirs[dir]
      i += 1

    if dir in verticals:
      step += 1
    
    dir = nextdir(dir)
  
  return coords


def manhattandistance(x1, x2):
  return sum([abs(x - y) for x,y in zip(x1, x2)])



def getstep(coords):
  """Returns the value of the step at coordinates coords"""
  #Finding value of step currently on
  if coords[1] > coords[0]:
    if coords[1] >= -coords[0]:
      return 2 * abs(coords[1])
    else:
      return 2 * abs(coords[0])
  elif coords[1] < coords[0]:
    if coords[1] <= -coords[0]:
      return 2 * abs(coords[1]) + 1
    else:
      return 2 * abs(coords[0]) - 1
  else:
    if coords[1] > 0:
      return 2 * abs(coords[1]) - 1
    elif coords[1] < 0:
      return 2 * abs(coords[1])
    else:
      return 0



def findcorner(step):
  """Finds next corner at which step changes based on current step"""
  if step == 0:
    return 1
  else:
    return findcorner(step - 1) + 2 * step

def invcoordinates(coords):
  """Returns the value at coordinates coords"""
  return findcorner(getstep(coords)) - manhattandistance(coords, getcoordinates(findcorner(getstep(coords))))


def getvalue(x, y, vals):
    if y >= x:
      return 0
    else:
      return vals[y-1]

def writevalue(x, vals):
  """Gets the value to be written at x as defined as the sum of its adjacents"""
  if vals == [] and x == 1:
    return 1
  coords = getcoordinates(x)
  adjacents = [[coords[0] + x, coords[1] + y] for x in [-1, 0, 1] for y in [-1, 0, 1]]
  
  return sum([getvalue(x, invcoordinates(i), vals) for i in adjacents])



#actual computation
print(manhattandistance(getcoordinates(inval), [0,0]))
vals = [1]
i = 2
while vals[-1] <= inval:
  vals.append(writevalue(i, vals))
  i += 1

print(vals[-1])




#########################
"""Less Hacky way??"""
import math


def goodgetcoords(x):
  level = math.floor(math.sqrt(x))
  corner = level ** 2
  coords = [level, 0]
  if x < corner + level + 1:
    coords[1] = x - corner
  if x < corner + 2 * level + 1:
    coords[0] = x - corner - level - 1
    coords[1] = level + 1
  if x < corner + 3 * level + 1:
    coords[0] = 0
    coords[1] = x - corner - 2 * level - 1
  else:
    coords[0] = x - corner - 3 * level - 1
  
  coords[0] -= (level - 1) / 2
  coords[1] -= (level - 1) / 2
  return coords

for i in range(1, 100):
  print(goodgetcoords(i))
  #if goodgetcoords(i) != getcoordinates(i):
  #  print(False)