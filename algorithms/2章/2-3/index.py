# 2-3-2

### 同一の実体であるため、同じIDが割り当てられる
# x = [1, 2, 3]
# y = x
# print(id(x)) 
# print(id(y)) 

### 同一の実体ではないため、異なるIDが割り当てられる
# x = [1, 2, 3]
# print(id(x))
# x = [4,5,6]
# print(id(x))

## 関数やメソッドの引数

### 呼び出し元の変数xと呼び出された関数内のxが同じ実体である

# def my_func(x):
#   print(id(x))

# x = [1, 2, 3]
# print(id(x))
# my_func(x)

# 2-3-3

## 3の倍数を格納するリストを返す関数
def my_func():
  numbers = []
  for i in range(100):
    if i % 3 == 0:
      numbers.append(i)
  return numbers

## 3の倍数の合計を計算する関数
def main():
  numbers = my_func()
  my_sum = 0
  for number in numbers:
    my_sum += number
  print(my_sum)

main()

## 改善①
def main():
  my_sum = 0
  for i in range(100):
    if i % 3 == 0:
      my_sum += i
  print(my_sum)

main()

## 改善②
def my_func():
  for i in range(100):
    if i % 3 == 0:
      yield i

def main():
  numbers = my_func()
  my_sum = 0
  for number in numbers:
    my_sum += number
  print(my_sum)

main()
    