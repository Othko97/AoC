def getfirewall(lines):
  poses = list(map(int, [line.split(": ")[0] for line in lines]))
  ranges = list(map(int, [line.split(": ")[1][:-1] for line in lines]))
  firewall = []
  for i in range(max(poses)+1):
    if i in poses:
      firewall.append(ranges[poses.index(i)])
    else:
      firewall.append(0)
  return firewall


def nextstep(pos, poses, dirs, firewall):
  pos += 1

  if poses[pos] == 0:
    severity = pos * firewall[pos]
    if pos == 0:
      severity = 1
  else:
    severity = 0

  for i in range(len(poses)):
    poses[i] += dirs[i]
    if poses[i] == firewall[i] - 1 or poses[i] == 0:
      dirs[i] *= -1
  
  return [pos, poses, dirs, severity]
  

def calcseverity(firewall):
  severity = 0
  pos = -1
  poses = [0 for i in firewall]
  dirs = []

  for i in firewall:
    if i == 0:
      dirs.append(0)
    else:
      dirs.append(1)

  for i in firewall:
    nextiter = nextstep(pos, poses, dirs, firewall)
    pos = nextiter[0]
    poses = nextiter[1]
    dirs = nextiter[2]
    severity += nextiter[3]
  return severity

def delay(time, firewall):
  pos = -1
  poses = [0 for i in firewall]
  dirs = []
  severity = 0

  for i in firewall:
    if i == 0:
      dirs.append(0)
    else:
      dirs.append(1)

  for i in range(time):
    poses = nextstep(pos, poses, dirs, firewall)[1]
  
  for i in firewall:
    nextiter = nextstep(pos, poses, dirs, firewall)
    pos = nextiter[0]
    poses = nextiter[1]
    dirs = nextiter[2]
    severity += nextiter[3]
  return severity
  



with open("../data/day13.txt", "r") as data:
  lines = data.readlines()

firewall = getfirewall(lines)
print(calcseverity(firewall))

i = -1
severity = -1
while severity != 0:
  i += 1
  severity = delay(i, firewall)
  print(severity)

print(i)