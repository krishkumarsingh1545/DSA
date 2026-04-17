class Node:
    def __init__(self, val: int):
        self.prev = None
        self.item = val
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        while True:
            print("\n----------------------------")
            print("1. Insert At Head")
            print("2. Insert At Tail")
            print("3. Delete At Head")
            print("4. Delete At Tail")
            print("5. Traverse")
            print("6. Reverse Traverse")
            print("(Press any key to exit)")
            print("----------------------------")
            print("Enter an option: ")
            match (int(input())):
                case 1:
                    self.insert_at_head(int(input("Enter the value: ")))
                case 2:
                    self.insert_at_tail(int(input("Enter the value: ")))
                case 3:
                    self.delete_at_head()
                case 4:
                    self.delete_at_tail()
                case 5:
                    self.printList()
                case 6:
                    self.printRevList()
                case _:
                    break
    
    def insert_at_head(self, val: int):
        newNode = Node(val)
        newNode.next = self.head
        if self.head != None:
            self.head.prev = newNode
        self.head = newNode
    
    def insert_at_tail(self, val: int):
        newNode = Node(val)
        if self.head == None:
            head = newNode
        currNode = self.head
        while currNode.next != None:
            currNode = currNode.next
        newNode.prev = currNode
        currNode.next = newNode

    def delete_at_tail(self):
        currNode = self.head
        while currNode.next.next != None:
            currNode = currNode.next
        currNode.next.prev = None
        currNode.next = None
    
    def delete_at_head(self):
        self.head = self.head.next
        self.head.prev = None
    
    def printList(self):
        if self.head == None:
            print("List is empty")
        currNode = self.head
        while currNode != None:
            print(currNode.item, " -> ", end="")
            currNode = currNode.next
        print("null")
        
    def printRevList(self):
        if self.head == None:
            print("List is empty")
        currNode = self.head
        while currNode.next != None:
            currNode = currNode.next
        while currNode != None:
            print(currNode.item, " -> ", end="")
            currNode = currNode.prev
        print("null")

ll = DoublyLinkedList()
