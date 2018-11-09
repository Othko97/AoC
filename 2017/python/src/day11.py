def getpathlength(path):
  #path = pathstring.split(",")
  bins = {'n':0, 'ne':0, 'se':0, 's':0, 'sw':0, 'nw':0}
  for i in path:
    bins[i] += 1

  ns = min([bins['n'], bins['s']])
  bins['n'] -= ns
  bins['s'] -= ns

  nesw = min([bins['ne'], bins['sw']])
  bins['ne'] -= nesw
  bins['sw'] -= nesw

  nwse = min([bins['nw'], bins['se']])
  bins['nw'] -= nwse
  bins['se'] -= nwse

  nenw = min([bins['ne'], bins['nw']])
  bins['n'] += nenw
  bins['ne'] -= nenw
  bins['nw'] -= nenw
  
  sesw = min([bins['se'], bins['sw']])
  bins['s'] += sesw
  bins['se'] -= sesw
  bins['sw'] -= sesw

  nes = min([bins['ne'], bins['s']])
  bins['se'] += nes
  bins['ne'] -= nes
  bins['s'] -= nes

  swn = min([bins['sw'], bins['n']])
  bins['nw'] += swn
  bins['n'] -= swn
  bins['sw'] -= swn

  nws = min([bins['nw'], bins['s']])
  bins['sw'] += nws
  bins['nw'] -= nws
  bins['s'] -= nws

  sen = min([bins['se'], bins['n']])
  bins['ne'] += sen
  bins['ne'] -= sen
  bins['n'] -= sen

  steps = [abs(bins['n'] - bins['s']), abs(bins['nw'] - bins['se']), abs(bins['ne'] - bins['sw'])]
  print(bins)

  return sum(steps)

def maxpathlength(path):
  maxval = 0
  maxindex = 0
  for i in range(len(path)+1):
    pathlength = getpathlength(path[:i])
    if pathlength > maxval:
      maxval = pathlength
      maxindex = i
  print([maxindex, maxval])

test1 = "ne,ne,ne".split(",")
test2 = "ne,ne,sw,sw".split(",")
test3 = "ne,ne,s,s".split(",")
test4 = "se,sw,se,sw,sw".split(",")

maxpathlength(test1)
maxpathlength(test2)
maxpathlength(test3)
maxpathlength(test4)

with open("../data/day11.txt") as data:
  pathstring = data.readline()

path = pathstring.split(",")

print(len(path))

maxpathlength(path)

