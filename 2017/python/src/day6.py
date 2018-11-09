import copy

def reallocate(l):
  """Reallocate blocks evenly from the maximum"""
  maxpos = l.index(max(l))
  noblocks = l[maxpos]
  l[maxpos] = 0
  i = 1
  while i <= noblocks:
    l[(maxpos + i) % len(l)] += 1
    i += 1
  
def findloop(l):
  """Finds number of iterations before a previous state turns up"""
  temp = copy.copy(l)
  reallocate(temp)
  prevstates = [l]
  n = 1
  while temp not in prevstates:
    prevstates.append(copy.copy(temp))
    reallocate(temp)
    n += 1
  x = prevstates.index(temp)
  return [n, len(prevstates) - x]

with open('../data/day6.txt', 'r') as data:
  banks = list(map(int, data.readline().split()))

print(findloop(banks))