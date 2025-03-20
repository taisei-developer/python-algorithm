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

my_list = [1, 3, 5, 6, 4, 2]
N = len(my_list) #=> 6
idx = 0
while idx < N and my_list[idx] <= 4:
    idx += 1

print(idx)


