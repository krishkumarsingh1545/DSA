import java.util.Scanner;

public class StackN {
    static class Stack {
        private int[] arr;
        private int top = -1;

        Stack(int size) {
            arr = new int[size];
            Scanner sc = new Scanner(System.in);
            while (true) {
                System.out.println("\n-----------------------------------");
                System.out.println("1. Peek");
                System.out.println("2. Push");
                System.out.println("3. Pop");
                System.out.println("4. Press any key to exit");
                System.out.println("-----------------------------------");
                System.out.print("Enter any option: ");
                switch (sc.nextInt()) {
                    case 1:
                        peek();
                        break;
                    case 2:
                        System.out.print("Enter the element: ");
                        push(sc.nextInt());
                        break;
                    case 3:
                        pop();
                        break;
                    default:
                        return;
                }
            }
        }

        boolean isEmpty() {
            if (top == -1)
                return true;
            return false;
        }

        boolean isFull() {
            if (top == arr.length-1)
                return true;
            return false;
        }
        
        void push(int item) {
            if (!isFull()) {
                arr[++top] = item;
                return;
            }
            System.out.println("Stack overflow");
        }
        
        void pop() {
            if (!isEmpty()) {
                System.out.println(arr[top--]);
                return;
            }
            System.out.println("Stack Underflow");
        }

        void peek() {
            if (!isEmpty()) {
                System.out.println("Top: " + arr[top]);
                return;
            }
            System.out.println("Stack is empty");
        }
    }
    public static void main(String[] args) {
        Stack foo = new Stack(4);
    }
}