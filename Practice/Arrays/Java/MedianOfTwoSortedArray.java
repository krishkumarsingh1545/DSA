public class MedianOfTwoSortedArray {
    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] result = new int[nums1.length + nums2.length];
        int i = 0, j = 0, k = 0;

        while (i < nums1.length && j < nums2.length) {
            if (nums1[i] <= nums2[j]) {
                result[k++] = nums1[i++];
            }
            else {
                result[k++] = nums2[j++];
            }
        }

        while (i < nums1.length) result[k++] = nums1[i++];
        while (j < nums2.length) result[k++] = nums2[j++];

        double med = 0;
        if (result.length%2 != 0) {
            med = result[result.length/2];
        }
        else {
            med = (double)(result[result.length/2] + result[(result.length/2)-1])/2;
        }
        System.out.println(result.length);
        System.out.println((result[result.length/2 - 1] + result[(result.length/2)])/2);
        System.out.println((result[result.length/2 + 1] + " " + result[(result.length/2)]));
        return med;
    }

    public static void main(String[] args) {
        int[] nums1 = {1, 2};
        int[] nums2 = {3, 4};
        System.out.println(findMedianSortedArrays(nums1, nums2));

    }
}