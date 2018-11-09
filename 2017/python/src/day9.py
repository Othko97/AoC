def score(s):
  garbage = False
  grouplevel = 0
  i = 0
  score = 0

  while i < len(s):
    char = s[i]
    if char == "!":
      i += 2
      continue
    if char == "<":
      garbage = True
    if char == ">":
      garbage = False
    if garbage == False and char == "{":
      grouplevel += 1
    if garbage == False and char == "}" and grouplevel > 0:
      score += grouplevel
      grouplevel -= 1
    i += 1
  
  return score

def garbagechars(s):
  garbage = False
  grouplevel = 0
  i = 0
  gchars = 0

  while i < len(s):
    starter = False
    char = s[i]
    if char == "!":
      i += 2
      continue
    if char == "<":
      if garbage == False:
        starter = True
      garbage = True
    if char == ">":
      garbage = False
    if garbage == False and char == "{":
      grouplevel += 1
    if garbage == False and char == "}" and grouplevel > 0:
      grouplevel -= 1
    if garbage == True and not starter:
      gchars += 1
    i += 1
  
  return gchars

with open("../data/day9.txt", "r") as data:
  stream = data.readlines()

for s in stream:
  #print(score(s[:-1]))
  print(garbagechars(s[:-1]))