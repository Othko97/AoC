bins = {}

def parse(line):
  els = line[:-1].split()

  #handle registers
  reg1 = els[0]
  reg2 = els[4]
  if reg1 not in bins.keys():
    bins[reg1] = 0
  if reg2 not in bins.keys():
    bins[reg2] = 0
  
  #handle binary operation
  op = els[1]
  
  #handle condition
  con = els[5]

  #handle values
  val1 = int(els[2])
  val2 = int(els[6])

  #logic section
  if op == 'inc':
    if con == "==":
      if bins[reg2] == val2:
        bins[reg1] += val1
    elif con == "<=":
      if bins[reg2] <= val2:
        bins[reg1] += val1
    elif con == "<":
      if bins[reg2] < val2:
        bins[reg1] += val1
    elif con == "!=":
      if bins[reg2] != val2:
        bins[reg1] += val1
    elif con == ">=":
      if bins[reg2] >= val2:
        bins[reg1] += val1
    elif con == ">":
      if bins[reg2] > val2:
        bins[reg1] += val1
    else:
      raise ValueError("Invalid condition")

  elif op == 'dec':
    if con == "==":
      if bins[reg2] == val2:
        bins[reg1] -= val1
    elif con == "<=":
      if bins[reg2] <= val2:
        bins[reg1] -= val1
    elif con == "<":
      if bins[reg2] < val2:
        bins[reg1] -= val1
    elif con == "!=":
      if bins[reg2] != val2:
        bins[reg1] -= val1
    elif con == ">=":
      if bins[reg2] >= val2:
        bins[reg1] -= val1
    elif con == ">":
      if bins[reg2] > val2:
        bins[reg1] -= val1
    else:
      raise ValueError("Invalid condition")

  else:
    raise ValueError("Invalid operation")

with open("../data/day8.txt", "r") as data:
  lines = data.readlines()

maxval = 0
for line in lines:
  try:
    parse(line)
    if max(bins.values()) > maxval:
      maxval = max(bins.values())
  except ValueError:
    print("Error!")

print(max(bins.values()))
print(maxval)