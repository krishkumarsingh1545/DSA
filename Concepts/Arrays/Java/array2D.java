public class array2D {

    public static void main(String[] args) {
        int arr[][] = {{3, 23, 54, 43},
                     {2, 25, 78, 458},
                     {32, 40, 23, 64}};
        
        // int sizeX = arr.length;
        // int sizeY = arr[0].length;

        for (int[] is : arr) {
            for (int is2 : is) {
                System.out.printf("%d ", is2);
            }
        }
    }
}