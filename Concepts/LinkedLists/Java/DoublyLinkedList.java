import java.util.Scanner;
public class DoublyLinkedList {

    DoublyLinkedList() {
        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.println("\n----------------------------");
            System.out.println("1. Insert At Head");
            System.out.println("2. Insert At Tail");
            System.out.println("3. Delete At Head");
            System.out.println("4. Delete At Tail");
            System.out.println("5. Traverse");
            System.out.println("6. Reverse Traverse");
            System.out.println("(Press any key to exit)");
            System.out.println("----------------------------");
            System.out.println("Enter an option: ");
            switch (sc.nextInt()) {
                case 1:
                    System.out.println("Enter the value: ");
                    insertAtHead(sc.nextInt());
                    break;
                    case 2:
                    System.out.println("Enter the value: ");
                    insertAtTail(sc.nextInt());
                    break;
                case 3:
                    deleteAtHead();
                    break;
                case 4:
                    deleteAtTail();
                    break;
                case 5:
                    print();
                    break;
                case 6:
                    revPrint();
                    break;
                default:
                    return;
            }
        }
    }
    static class Node {
        Node prev;
        int data;
        Node next;

        Node(int item) {
            prev = null;
            data = item;
            next = null;
        }
    }

    Node head;

    void insertAtHead(int item) {
        Node newNode = new Node(item);
        if (head != null) {
            head.prev = newNode;
        }
        newNode.next = head;
        head = newNode;
        
    }

    void insertAtTail(int item) {
        Node newNode = new Node(item);
        if (head == null) {
            head = newNode;
            return;
        }
        Node currNode = head;
        while (currNode.next != null)
            currNode = currNode.next;
        newNode.prev = currNode;
        currNode.next = newNode;
    }
    
    void deleteAtHead() {
        Node temp = head;
        head = head.next;
        head.prev = null;
        temp = null;
    }
    
    void deleteAtTail() {
        Node currNode = head;
        while (currNode.next.next != null)
            currNode = currNode.next;
        currNode.next.prev = null;
        currNode.next = null;
    }
    
    void print() {
        Node currNode = head;
        while (currNode != null) {
            System.out.print(currNode.data + " -> ");
            currNode = currNode.next;
        }
        System.out.print("null\n");
    }

    void revPrint() {
        Node currNode = head;
        while (currNode.next != null) {
            currNode = currNode.next;
        }
        while (currNode != null) {
            System.out.print(currNode.data + " -> ");
            currNode = currNode.prev;
        }
        System.out.print("null\n");
    }


    public static void main(String[] args) {
        DoublyLinkedList foo = new DoublyLinkedList();
    }
}