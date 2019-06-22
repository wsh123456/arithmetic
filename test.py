from arithmetic.LinkedListQueue import LinkedListQueue
from arithmetic.MyQueue import LoopQueue, ArrayQueue
import time


def testQueue(queue, opCount):
    startTime = int(time.time() * 1000)
    testq = queue()
    for i in range(opCount):
        testq.enqueue(i)
    for i in range(opCount):
        testq.dequeue()

    endTime = int(time.time() * 1000)
    return (endTime - startTime) / 1000


opCount = 10000
time1 = testQueue(ArrayQueue, opCount)
print("ArrayQueue : ", time1, " s")
time2 = testQueue(LoopQueue, opCount)
print("LoopQueue : ", time2, " s")
time3 = testQueue(LinkedListQueue, opCount)
print("LinkedListQueue : ", time3, " s")