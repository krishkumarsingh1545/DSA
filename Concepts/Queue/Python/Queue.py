class Queue:
    arr: list = []
    rear: int = -1
    front: int = -1

    def __init__(self, size: int):
        self.size = size
        self.arr: list = []
        while True:
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Peek Front")
            print("4. Peek Rear")
            print("(Press any key to end)")
            match int(input("Enter any option: ")):
                case 1:
                    self.enq(int(input("Enter item: ")))
                case 2:
                    self.deq()
                case 3:
                    self.peekF()
                case 4:
                    self.peekR()
                case _:
                    print("Terminated")
                    exit()
    
    def enq(self, item: int):
        if self.rear == self.size - 1:
            print("Queue Overflow")
            return
        if self.front == -1: self.front = 0
        # if self.rear == -1: self.rear = 0
        self.rear+=1
        self.arr.append(item)
    
    def deq(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Underflow")
            return
        print("--------------------------------")
        print("Dequeue:", self.arr[self.front])
        print("--------------------------------")
        self.front+=1

    def peekF(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue is empty")
            return
        print("--------------------------------")
        print("Front:", self.arr[self.front])
        print("--------------------------------")

    def peekR(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue is empty")
            return
        print("--------------------------------")
        print("Rear:", self.arr[self.rear])
        print("--------------------------------")

q = Queue(int(input("Enter the size: ")))