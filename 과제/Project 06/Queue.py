class Queue(object):
    def __init__(self):
        self.queue = []

    def dequeue(self):
        if len(self.queue) == 0:
            return -1
        return self.queue.pop(0)

    def enqueue(self, pos):
        self.queue.append(pos)
        pass

    def printQueue(self):
        print(self.queue)


if __name__ == "__main__":
    q = Queue()
    q.enqueue((10, 20))
    q.enqueue((20, 30))
    q.enqueue((40, 50))
    q.enqueue((50, 70))
    q.printQueue()

    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.printQueue()
