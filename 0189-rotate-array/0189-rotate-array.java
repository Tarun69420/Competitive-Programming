class Solution {
    public void rotate(int[] nums, int k) {
        k = k%(nums.length);
        int half = nums.length - k;
        rev(nums,0,half-1);
        //System.out.println(nums[k+1]);
        rev(nums,half,nums.length-1);
        //System.out.println(nums[k+1]);
        rev(nums,0,nums.length-1);
    }
    public static void rev(int [] arr , int l,int r)
    {
        while (l<r)
        {
            int temp = arr[l];
            arr[l] = arr[r];
            arr[r] = temp;
            l++;
            r--;
        }

    }
}