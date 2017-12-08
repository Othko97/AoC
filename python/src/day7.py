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
  # while tower has children with different weights
  while not balanced(tower):
    base = tower.max_stack()
    childtowers = [getsubtower(tower, findbyname(tower, name))
                   for name in base.children]
    for child in childtowers:
      imbalanced = False
      # if child has children with different weights
      if not balanced(child):
        imbalanced = True
        prev = tower
        tower = child
        break
 
    # this tower is unbalanced and none of its children are, one of the
    # children must be causing the problem
    if imbalanced == False:
      break
 
  # Here tower is the tower with bad as a child.
  # we need to identify which child is bad; it is the only one whose weight
  # only occurs once.
  childtowers = [getsubtower(tower, findbyname(tower, name))
                 for name in tower.max_stack().children]
  child_weights = [child.weight for child in childtowers]
 
  # enumerate the weights, and find the correct one (appears > 1 times)
  # and the bad one (appears only once)
  for idx, weight in enumerate(child_weights):
    occurrences = [w for w in child_weights if w == weight]
    # these checks only make sense if there is more than one element
    if len(childtowers) > 1 and len(occurrences) > 1:
      target = weight
    elif len(childtowers) > 1 and len(occurrences) == 1:
      bad = childtowers[idx]
 
  # diff is target (a good sibling's total weight) - the bad tower's
  # total weight
  diff = target - bad.weight
 
  # return bad tower's base element's weight plus the difference (with the
  # test data, this is 68 + -8)
  return bad.max_stack().weight + diff


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