# Contest: https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a
# Problem: https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d12d7
# Attempts: 1
# Solved: during contest

import numpy as np

T = int(input())

for t in range(1, T+1):
  n, c = map(int, input().split())
  minc = n - 1
  maxc = n * (n + 1) / 2 - 1
  
  res = 'IMPOSSIBLE'
  if c >= minc and c <= maxc:
    res = [-1] * n
    resi = np.array(range(n))
    i = 0
    while c != 0:
      curr_max_cost = n - i
      next_min_cost = n - (i + 1) - 1
      if c - curr_max_cost - next_min_cost >= 0:
        curr_cost = curr_max_cost
      else:
        curr_cost = c - next_min_cost
        
      mini = i + curr_cost - 1
      
      res[resi[mini]] = i + 1
      resi[i : mini + 1] = resi[i : mini + 1][::-1]
      
      c -= curr_cost
      i += 1  

    while i < n:
      res[resi[i]] = i + 1
      i += 1
      
  
  if res != 'IMPOSSIBLE':
    res = ' '.join(map(str, res))
  print(f'Case #{t}: {res}')