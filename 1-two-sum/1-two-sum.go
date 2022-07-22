func twoSum(nums []int, target int) []int {
    set := map[int]int{}
    for i, num := range nums {
        set[num] = i
    }
    
    for i, num := range nums {
        if targetIndex, ok := set[target - num]; ok && targetIndex != i {
            return []int {i, targetIndex}
        }
    }
    
    return []int{}
}