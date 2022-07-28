func productExceptSelf(nums []int) []int {
    ans := make([]int, len(nums))
    ans[0] = 1
    
    for i := 1; i < len(nums); i++ {
        ans[i] = ans[i - 1] * nums[i - 1]
    }
    
    prod := 1
    for i := len(nums) - 1; i >= 0; i-- {
        ans[i] = ans[i] * prod
        prod = nums[i] * prod
    }
    
    return ans
}