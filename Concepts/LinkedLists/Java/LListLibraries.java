import java.util.LinkedList;

public class LListLibraries {
    public static void main(String[] args) {
        LinkedList<Integer> ll = new LinkedList<Integer>();
        LinkedList<Integer> l2 = new LinkedList<Integer>();
        LinkedList<Integer> l3 = new LinkedList<Integer>();
        ll.add(2);
        ll.add(22);
        ll.add(222);
        ll.add(2222);
        l2.add(3);
        l2.add(33);
        l2.add(333);
        l2.add(3333);
        l2.add(33333);
        ll = ll.reversed();
        l2 = l2.reversed();
        for (Integer i : ll) {
            for (Integer j : l2) {
                System.out.println(i+j);
            }
        }
        System.out.println(l3);
    }
}