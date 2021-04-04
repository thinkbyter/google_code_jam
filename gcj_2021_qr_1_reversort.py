# Contest: https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a
# Problem: https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c
# Attempts: 1
# Solved: during contest

import numpy as np

T = int(input())

for t in range(1, T+1):
  n = int(input())
  xs = np.array(list(map(int, input().split())))
  
  cost = 0
  for i in range(n - 1):
    icost = np.argmin(xs[i:]) + 1

    cost += icost
    mini = i + icost 
    xs[i : mini] = xs[i : mini][::-1]
    
  print(f'Case #{t}: {cost}')