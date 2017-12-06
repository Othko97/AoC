def checksum1(table):
  """Takes the checksum of as defined in the problem - using max - min in row"""
  sum = 0
  for row in table:
    sum += max(row) - min(row)
  return sum

def divisibleby(a, b):
  """Returns a|b"""
  return (b/a).is_integer()

def checksum2(table):
  sum = 0
  for row in table:
    for i in range(len(row)):
      for j in range(len(row)):
        if divisibleby(row[j], row[i]) and i != j:
          sum += int(row[i]/ row[j])
  return sum

with open("../data/day2.txt") as data:
  strings = data.readlines()
table=[]
for row in strings:
  if row != strings[-1]:
    table.append(list(map(int, row[:-1].split("\t"))))
  else:
    table.append(list(map(int, row.split("\t"))))

maxes = [max(row) for row in table]
mins = [min(row) for row in table]
s = sum([x-y for x,y in zip(maxes, mins)])

print(checksum1(table))
print(checksum2(table))