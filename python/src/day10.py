def twist(circlist, length, current):
  sublist = []
  for i in range(length):
    sublist.append(circlist[(current + i) % len(circlist)])
  sublist.reverse()
  for i in range(length):
    circlist[(current + i) % len(circlist)] = sublist[i]
  return circlist

def fullthrough(circlist, lengths, current, skipsize):
  for l in lengths:
    circlist = twist(circlist, l, current)
    current += l + skipsize
    skipsize += 1
  return [circlist, current, skipsize]

def knothash(string):
  circlist = list(range(256))
  lengths = [ord(x) for x in string]
  lengths += [17, 31, 73, 47, 23]
  current = 0
  skipsize = 0
  for i in range(64):
    oneround = fullthrough(circlist, lengths, current, skipsize)
    circlist = oneround[0]
    current = oneround[1]
    skipsize = oneround[2]
  
  dense = []
  for i in range(0, 255, 16):
    sublist = circlist[i:i+16]
    x = 0
    for i in sublist:
      x = x ^ i
    dense.append("{:02x}".format(x))
  
  hashed = "".join(dense)
  return hashed



test = [0,1,2,3,4]
testlens = [3,4,1,5]

testhashed = fullthrough(test, testlens, 0, 0)



circlist = list(range(256))
with open("../data/day10.txt", "r") as data:
  lengths = list(map(int, data.readline().split(",")))
  data.seek(0)
  puzzlein = data.readline()

#hashed = fullthrough(circlist, lengths, 0, 0)

#print(hashed[0] * hashed[1])
print()
print(knothash(""))
print(knothash("AoC 2017"))
print(knothash("1,2,3"))
print(knothash("1,2,4"))
print(knothash(puzzlein))