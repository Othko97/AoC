def connect(previter, relations):
  current = previter.copy()
  for i in previter:
    for j in relations[i]:
      current.add(j)
  return current

def connectcomponent(node, relations):
  component = set([node])
  while component < connect(component, relations):
    component = connect(component, relations).copy()
  return component

def toconnectedcomponents(relations):
  components = set([])
  for i in range(len(relations)):
    components.add(frozenset(connectcomponent(i, relations)))
  return components

with open("../data/day12.txt") as data:
  inputs = data.readlines()

relations = [list(map(int, line[:-1].split(" <-> ")[1].split(","))) for line in inputs]

print(len(connectcomponent(0, relations)))
print(len(toconnectedcomponents(relations)))