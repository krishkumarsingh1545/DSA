import os
class Stack:
    arr: list = []
    top: int = -1
    size: int = -1

    def __init__(self, size: int):
        self.size = size
        while True:
            # os.system('cls')
            print("\n-----------------------------------")
            print("1. Peek")
            print("2. Push")
            print("3. Pop")
            print("4. Show")
            print("5. Press any key to exit")
            print("-----------------------------------")
            op = int(input("Enter option: "))
            print("-----------------------------------\n")
            match op:
                case 1:
                    self.peek()
                case 2:
                    self.push(int(input("Enter value to push: ")))
                case 3:
                    self.pop()
                case 4:
                    self.show()
                case _:
                    print("Terminated")
                    exit()

    def push(self, item: int):
        if self.top == self.size-1:
            print("Stack overflow")
            return
        self.top += 1
        self.arr.append(item)

    def pop(self):
        if self.top == -1:
            print("Stack underflow")
        print(self.arr[self.top])
        self.top -= 1
    
    def peek(self):
        if self.top == -1:
            print("Stack is empty")
            return
        print(self.arr[self.top])

    def show(self):
        if self.top == -1:
            print("Stack is empty")
            return
        for i in self.arr:
            print(i, end=' ')
        

s1 = Stack(4)

