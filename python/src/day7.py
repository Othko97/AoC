def findbyname(tower, name):
  for e in tower.elements:
    if e.name == name:
      return e

def get_stack(tower, element):
  stack = [element]
  for x in element.children:
    stack += get_stack(tower, findbyname(tower, x))
  return stack

def getsubtower(tower, element):
  return Tower(get_stack(tower, element))

def balanced(tower):
  if tower.length == 1:
    return True
  else:
    base = tower.max_stack()
    childtowers = [getsubtower(tower, findbyname(tower, name)) for name in base.children]
    for t in childtowers:
      if t.weight != childtowers[0].weight:
        return False
    return True

def balance(tower):
  prev = tower
  while not balanced(tower):
    base = tower.max_stack()
    childtowers = [getsubtower(tower, findbyname(tower, name)) for name in base.children]
    for t in childtowers:
      imbalanced = False
      if not balanced(t):
        imbalanced = True
        prev = tower
        tower = t
        break

    if imbalanced == False:
      break

  childtowers = [getsubtower(prev, findbyname(prev, name)) for name in prev.max_stack().children]

  if childtowers[0] == tower:
    s = childtowers[1]
  else:
    s = childtowers[0]
  
  
  diff = tower.weight - s.weight
  print(balanced(tower))
  for x in [getsubtower(tower, findbyname(tower, name)) for name in base.children]:
    print(x.weight)
  print(tower.weight)
  print(s.weight)
  print(tower.max_stack().weight)
  return tower.max_stack().weight - diff


class TowerElement():
  def __init__(self, name, weight, children):
    self.name = name
    self.weight = weight
    self.children = children

class Tower():
  def __init__(self, elements):
    self.elements = elements
    self.weight = sum([e.weight for e in elements])
    self.length = len(elements)

  def max_stack(self):
    return self.sort()[0]

  def sort(self):
    return sorted(self.elements, key = lambda x: getsubtower(self, x).length, reverse=True)



with open("../data/day7.txt", "r") as data:
  lines = data.readlines()

elements = []
for element in lines:
  name = element.split()[0]
  weight = int(element.split("(")[1].split(")")[0])
  if " -> " in element:
    children = element[:-1].split(" -> ")[1].split(", ")
  else:
    children = []
  elements.append(TowerElement(name, weight, children))

tower = Tower(elements)
print(tower.max_stack().name)
print(balance(tower))

#for e in tower.sort():
#  print(balanced(getsubtower(tower, e)))