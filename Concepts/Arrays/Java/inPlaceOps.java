public class inPlaceOps {
    
    public static void swap(int[] arr, int left, int right) {
        arr[left] += arr[right];
        arr[right] = arr[left] - arr[right];
        arr[left] -= arr[right];

    }
    public static void main(String[] args) {
        int[] arr = {3, 23, 54, 43 ,2, 25, 78, 458, 23, 64};
        int left = 0, right = arr.length-1;

        System.out.print("\nBefore Swap: ");
        for (int i : arr) {
            System.out.printf("%d ", i);
        }
        
        while (left < right) {
            swap(arr, left, right);
            left += 1;
            right -= 1;
        }
        
        System.out.print("\nAfter Swap: ");
        for (int i : arr) {
            System.out.printf("%d ", i);
        }
    }
}