func containsDuplicate(nums []int) bool {
    kv := make(map[int]struct{})
    for _, num := range nums {
        if _, ok := kv[num]; ok {
            return true
        }
        
        kv[num] = struct{}{}
    }
    
    return false
}