import java.util.Scanner;

public class QueueBucket {
    static class Queue {
        Scanner sc = new Scanner(System.in);
        private int[] arr;
        private int rear = -1, front = -1;

        Queue(int size) {
            arr = new int[size];
            while (true) {
                System.out.println("1. Enqueue");
                System.out.println("2. Dequeue");
                System.out.println("3. Peek Front");
                System.out.println("4. Peek Rear");
                System.out.println("(Press any key to end)");
                System.out.print("Enter option: ");
                switch (sc.nextInt()) {
                    case 1:
                        enq(sc.nextInt());
                        break;
                    case 2:
                        deq();
                        break;
                    case 3:
                        peekF();
                        break;
                    case 4:
                        peekR();
                        break;
                    default:
                        return;
                }
            }
        }

        void enq(int item) {
            if (rear == arr.length-1) {
                System.out.println("Queue Overflow");
                return;
            }
            if (front == -1) front = 0;
            arr[++rear] = item;
        }

        void deq() {
            if (front == -1 || front > rear) {
                System.out.println("Queue underflow");
                return;
            }
            System.out.println("Dequeue: " + arr[front++]);
        }
        
        void peekR() {
            if (front == -1 && front > rear) {
                System.out.println("Queue Empty");
                return;
            }
            System.out.println("-----------------------------");
            System.out.println("Front: " + arr[rear]);
            System.out.println("-----------------------------");
        }
        void peekF() {
            if (front == -1 && front > rear) {
                System.out.println("Queue Empty");
                return;
            }
            System.out.println("-----------------------------");
            System.out.println("Front: " + arr[front]);
            System.out.println("-----------------------------");
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size of queue: ");
        Queue foo = new Queue(sc.nextInt());
    }
}