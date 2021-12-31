public class Solution {
    public void Merge(int[] nums1, int m, int[] nums2, int n) {
        int curr = nums1.Length - 1;
        int left = m - 1, right = n - 1;
        
        while (left >= 0 && right >= 0)
        {
            nums1[curr--] = nums1[left] > nums2[right]
                ? nums1[left--]
                : nums2[right--];
        }
        
        while (left >= 0)
        {
            nums1[curr--] = nums1[left--];
        }
        
        while (right >= 0)
        {
            nums1[curr--] = nums2[right--];
        }
    }
}