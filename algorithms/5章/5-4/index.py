# 5-4-2

# 挿入ソート
def insertion_sort(my_list):
  # リストの先頭側からひとつずつ操作する
  for i in range(1, len(my_list)):

    # i番目の要素をソート対象として取り出す
    # i = 1のとき
    target = my_list[i] # target = 1

    # ソート済み部分のインデックス
    j = i - 1 # j = 0
    
    # 操作対象の要素より小さい値を持つ要素が見つかるまでひとつ右側にずらす
    # 0 <= 0 かつ 1 < 6 なので条件成立
    while 0 <= j and target < my_list[j]:

      # 要素をひとつ右側にずらす
      # 例：my_list[1] = 6 (6を右にずらす)
      my_list[j + 1] = my_list[j] # my_list[1] = 6
      
      # インデックスを左にずらす
      # 例：j = -1 (配列の先頭よりも左を指す。これによりターゲットが先頭に入ることを表現)
      j -= 1 # j = -1

    # ずらし終わったら、空いた位置に操作対象の要素を設定
    # 例：j = -1のとき、my_list[0] = 1 (先頭に1を挿入)
    my_list[j + 1] = target

    # 途中結果の確認のためダンプ
    print(my_list)

data = [6, 1, 4, 3, 2]
print(data)
insertion_sort(data)
print(data)