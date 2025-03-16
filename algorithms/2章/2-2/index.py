# 2-2-1

def is_prime(N):
  ## 素数判定に1は不要
  if N == 1:
    return False
  
  for i in range(2, N):
    ## 割り切れる数があれば素数ではない
    if N % i == 0:
      return False
  ## 割り切れる数がなければ素数 = 1 と 自分自身でしか割り切れない
  return True

result = is_prime(7)
print(result)

## 改善

import math

def is_prime(N):
  if N == 1:
    return False
  
  for i in range(2, int(math.sqrt(N)) + 1):
    if N % i == 0:
      return False
  return True

result = is_prime(24)
print(result)
    

# 2-2-2 オーダー記法
  
    