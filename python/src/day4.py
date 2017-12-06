with open("./data/day4.txt", 'r') as data:
  passphrases = data.readlines()

numbervalid = 0

for s in passphrases:
  s = s.split()
  valid = True
  for i in range(len(s)):
    for j in range(i+1, len(s)):
      if s[i] == s[j]:
        valid = False
  if valid == True:
    numbervalid += 1

print(numbervalid)


numbervalid = 0

for s in passphrases:
  s = s.split()
  valid = True
  for i in range(len(s)):
    for j in range(i+1, len(s)):
      if sorted(s[i]) == sorted(s[j]):
        valid = False
  if valid == True:
    numbervalid += 1
  

print(numbervalid)