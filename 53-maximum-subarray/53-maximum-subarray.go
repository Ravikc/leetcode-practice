func max(a, b int) int {
    if a > b {
        return a
    }
    
    return b
}

func maxSubArray(nums []int) int {
    ans := nums[0]
    maxSoFar := nums[0]
    
    for i := 1; i < len(nums); i++ {
        maxSoFar = max(nums[i], nums[i] + maxSoFar)
        ans = max(ans, maxSoFar)
    }
    
    return ans
}