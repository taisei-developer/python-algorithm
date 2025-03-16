# マルチスレッドと呼ばれる非同期処理を用いてデータを受け渡す

import threading
import queue
import time

q = queue.Queue()

def producer():
  """キューに処理対象データを追加"""
  print("producer: データ追加処理開始")

  ## データをエンキュー
  ## nは処理に要する時間で、順番に実行すると処理時間は14秒かかる
  q.put({ "task": "データ１", "n": 2})
  q.put({ "task": "データ２", "n": 3})
  q.put({ "task": "データ３", "n": 5})
  q.put({ "task": "データ4", "n": 4})
  print("producer: データ追加処理終了")

def worker():
  """キューからデータを取り出して、処理を実行"""
  while True:
    ## q.get()でキューからデータを取り出す
    item = q.get()
    
    ## 取り出したデータがNoneの場合、処理を終了
    if item is None:
      break

    print("worker:", item.get("task") + "の処理を開始します")
    time.sleep(item.get("n"))
    print("worker:", item.get("task") + "の処理を終了します")
    q.task_done()


