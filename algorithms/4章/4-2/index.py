# 4-2-1

# class MyStack:
#   def __init__(self):
#     self.data = []

#   def push(self, value):
#     self.data.append(value)

#   def pop(self):
#     return self.data.pop()

#   def __str__(self):
#     return str(self.data)

# my_stack = MyStack()

# ## データを順にpushする
# my_stack.push('a')
# print(my_stack)
# my_stack.push('b')
# print(my_stack)
# my_stack.push('c')
# print(my_stack)

# ## データを順にpopし、val1〜val3に格納する
# val1 = my_stack.pop()
# print(my_stack)
# val2 = my_stack.pop()
# print(my_stack)
# val3 = my_stack.pop()
# print(my_stack)

# # 取り出したデータを確認
# print(val1, val2, val3)

# 4-2-2

class FixedSizeStack:
  def __init__(self, N):
    self.N = N
    self.stack = [None] * N
    self.pointer = 0

  def push(self, value):
    if self.N <= self.pointer:
      ## スタックがいっぱいの場合はpush失敗
      print("スタックがいっぱいのため、pushできません")
      return
    
    self.stack[self.pointer] = value
    self.pointer += 1

  def pop(self):
    ## スタックが空の場合はpop失敗
    if self.pointer == 0:
      print("スタックが空のため、popできません")
      return
    
    value = self.stack[self.pointer - 1]
    self.stack[self.pointer - 1] = None
    self.pointer -= 1
    return value

  def __str__(self):
    return str(self.stack)

fixed_size_stack = FixedSizeStack(4)

## データを順にpushする
fixed_size_stack.push('a')
print(fixed_size_stack)
fixed_size_stack.push('b')
print(fixed_size_stack)
fixed_size_stack.push('c')
print(fixed_size_stack)

## データを順にpopし、val1〜val3に格納する
val1 = fixed_size_stack.pop()
print(fixed_size_stack)
val2 = fixed_size_stack.pop()
print(fixed_size_stack)
val3 = fixed_size_stack.pop()
print(fixed_size_stack)




    
    
    
    