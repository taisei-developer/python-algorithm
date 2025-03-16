class MyQueue:
  def __init__(self):
    self.que = []

  ## データを追加する
  def enqueue(self, value):
    self.que.append(value)
  
  ## データを取り出す
  def dequeue(self):
    return self.que.pop(0)
  
  ## 文字列表現を返す
  def __str__(self):
    return str(self.que)
    

q = MyQueue()

## データを順に追加する
q.enqueue('a')
print(q)
q.enqueue('b')
print(q)
q.enqueue('c')
print(q)

## データを順に取り出す
val1 = q.dequeue()
print(q)
val2 = q.dequeue()
print(q)
val3 = q.dequeue()
print(q)