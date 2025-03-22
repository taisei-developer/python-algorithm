# 5-3-1 ループ処理

## インデックスによるループ処理

my_list = [1, 2, 3]

# for val in my_list:
#     print(val)

# N = len(my_list)
# for idx in range(N):
#     print(my_list[idx])

## for-if-breakとwhile

# my_list = [1, 3, 5, 6, 4, 2]
# N = len(my_list)
# idx = None
# for i in range(N):
#     if 4 < my_list[i]:
#         idx = i
#         break

# print(idx)

# my_list = [1, 3, 5, 6, 4, 2]
# N = len(my_list) #=> 6
# idx = 0
# while idx < N and my_list[idx] <= 4:
#     idx += 1

# print(idx)


# my_list = [1, 3, 5, 6, 4, 2]
# N = len(my_list)
# idx = N - 1 #=> 5
# while idx >= 0 and my_list[idx] <= 4:
#     idx -= 2

# print(idx)

# 5-3-2 交換

x = 10
y = 20
x, y = y, x
print(x, y)

# 5-3-3 挿入

my_list = [1, 3, 4, 6, 2]
print(my_list)

# 3番目の要素を1番目に挿入
from_idx = 3
to_idx = 1

tmp = my_list.pop(from_idx)
my_list.insert(to_idx, tmp)
print(my_list)




