def getsteps(l):
  pos = 0
  steps = 0
  while pos < len(l):
    prev = pos
    pos = pos + l[pos]
    if l[prev] >= 3:
      l[prev] -= 1
    else:
      l[prev] += 1
    steps += 1
  return steps

with open('./data/day5.txt', 'r') as data:
  puzzleinput = [int(x) for x in data.readlines()]


print(getsteps(puzzleinput))