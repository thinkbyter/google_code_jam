# Contest: https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a
# Problem: https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1145
# Attempts: 1
# Solved: during contest

T = int(input())

for t in range(1, T+1):
  x, y, s = input().split()
  x = int(x)
  y = int(y)
  
  # CJ - x
  # JC - y
  # C?
  cost = 0
  pc = s[0]
  i = 1
  if i < len(s) and pc == '?':
    while i < len(s) and s[i] == '?':
      i += 1
      
    if i < len(s):
      pc = s[i]
      i += 1
  
  while i < len(s):
    c = s[i]
    
    if c == '?': # pc will always be a character, never '?'.
      while i < len(s) and s[i] == '?':
        i += 1
    else:
      if pc == 'C' and c == 'J':
        cost += x
      elif pc == 'J' and c == 'C':
        cost += y
        
      pc = c
      i += 1
  
  print(f'Case #{t}: {cost}')