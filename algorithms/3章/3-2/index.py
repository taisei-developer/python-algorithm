class Node:
  def __init__(self, value=None):
    self.value = value # 要素が保持する値
    self.next = None   # 次の要素への参照

  def __str__(self):
    return str(self.value) # 要素が保持する値を文字列に変換して返す

# 単連結リスト本体
class SinglyLinkedList:
  def __init__(self, head_value):
    self.head = Node(head_value) # リストの先頭要素を作成

  # 要素の追加
  def append(self, value):
    
    # 新たに要素を作成
    new_node = Node(value)

    # 先頭から順にリンクが設定されていない要素（終端ノード）まで辿る
    current_node = self.head
    while current_node.next:
      current_node = current_node.next

    # 辿った終端ノードのnextに生成した要素を設定
    current_node.next = new_node

  # 要素の表示
  def __str__(self):
    nodes = []
    current_node = self.head
    while current_node:
      nodes.append(current_node.value)
      current_node = current_node.next
    return str(nodes)
  
  # 要素の取得
  def get(self, idx):
    # 先頭idx番目まで要素を辿る
    current_node = self.head
    current_idx = 0
    while current_node and current_idx < idx:
      current_node = current_node.next
      current_idx += 1
    return current_node

  # 要素の挿入
  def insert(self, idx, value):
    # 新たな要素を作成
    new_node = Node(value)

    # 先頭への挿入の場合、headを付け替え
    if idx == 0:
      new_node.next = self.head
      self.head = new_node
      return
    
    # 先頭以外への挿入の場合、idxのひとつ目の要素を取得
    pre_node = self.get(idx - 1)

    # 指定した要素が見つからない場合は終了
    if not pre_node:
      print("指定した要素が見つかりません")
      return
    
    # 参照先を付け替え
    new_node.next = pre_node.next
    pre_node.next = new_node

  # 要素の削除
    
