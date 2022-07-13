func missingNumber(nums []int) int {
    n := len(nums)
    expectedSum := 0
    currentSum := 0
    for i:= 0; i < n; i++ {
        expectedSum += i
        currentSum += nums[i]
    }
    
    expectedSum += n
    
    return expectedSum - currentSum
    
}