import queue

check = queue.Queue(maxsize=1)

check.put('test')

check.put('blocked')  # this gets blocked # 2

# 2 will be blocked or tht thread waits until some other threads gets something out of queue
# since queue is filled


