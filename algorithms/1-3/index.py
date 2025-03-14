# 1-3-1 条件分岐

## 閏年の判定

# if N % 4 == 0:
#   if N % 100 == 0:
#     if N % 400 == 0:
#       print("400で割り切れるため、閏年です")
#     else:
#       print("100で割り切れるが、400で割り切れないため、平年です")
#   else:
#     print("4で割り切れるが、100で割り切れないため、閏年です")
# else:
#   print("4で割り切れないため、平年です")

# N = 2023

# if N % 4 != 0:
#   print("4で割り切れないため、平年です")
# elif N % 100 != 0:
#   print("100で割り切れないため、閏年です")
# elif N % 400 != 0:
#   print("400で割り切れないため、平年です")
# else:
#   print("閏年です")

N = 2023

if N % 4 == 0 and (N % 100 != 0 or N % 400 == 0):
  print("閏年です")
else:
  print("平年です")


# 1-3-2 関数ないでの分岐とアーリーリターン

def is_leap(year):
  if year % 4 != 0:
    return False
  elif year % 100 != 0:
    return True
  elif year % 400 != 0:
    return False
  else:
    return True

# 1-3-3 ループ処理

my_list = [1, 3, 2, 5, 4, 9]

max_value = my_list[0] # 1

for val in my_list[1:]:
  if max_value < val:
    max_value = val

print("最大値", max_value)

# 1-3-4 アーリーコンティニュー

## 偶数のみを処理する例
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("偶数のみを処理する例:")
for num in numbers:
    # 奇数の場合はスキップ
    if num % 2 != 0:
        continue
    # 偶数の場合のみ実行される処理
    print(f"{num}は偶数です")

# 1-3-5 while文

# 1-3-6 再帰処理

# 1-3-7 ダンプ

my_list = [1, 2, 3, 4, 5]
print(my_list)

x = 100
y = 200
z = [3, 1, 5]
print(x, y, z, sep="-")

my_text = str([3, 1, 5])
print(my_text)

text = "my_text"
num = 3
print(text + str(num))

text = "xの値は:{x}, yの値は:{y}"
x = 100
y = 200
print(text.format(x=x, y=y))

# 1-3-8 クラスの基礎

# class Cood:
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y

# # インスタンス化
# obj = Cood(300, 400)
# print(obj.x, obj.y)

# # インスタンス変数の変更
# obj.x = 1000
# print(obj.x, obj.y)

from math import sqrt

class Cood:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def calc_distance(self):
    return sqrt(self.x ** 2 + self.y ** 2)

obj = Cood(300, 400)
print(obj)
# => <__main__.Cood object at 0x100600000>
print(obj.calc_distance())








