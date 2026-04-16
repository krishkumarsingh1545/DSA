public class prefixSum {

    public static void main(String[] args) {
        int arr[] = {3, 23, 54, 43 ,2, 25, 78, 458, 23, 64};
        System.out.println(arr.length);
        for (int i = 1; i < arr.length; i++) {
            arr[i] += arr[i-1];
        }
        for (int i : arr) {
            System.out.printf("%d ", i);
        }
    }
}