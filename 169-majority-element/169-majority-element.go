func majorityElement(nums []int) int {
    num := nums[0]
    count := 1
    
    for i := 1; i < len(nums); i++ {
        if count == 0 {
            num = nums[i]
            count = 1
        } else if nums[i] == num {
            count += 1
        } else {
            count -= 1
        }
    }
    
    return num
}