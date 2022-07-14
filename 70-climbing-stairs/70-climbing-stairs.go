func find(steps int, memo map[int]int) int {
    if v, contains := memo[steps]; contains {
        return v
    }
    
    if steps == 0 {
        return 1
    }
    
    if steps < 0 {
        return 0
    }
    
    memo[steps - 1] = find(steps - 1, memo) 
    memo[steps - 2] = find(steps - 2, memo)
    return memo[steps - 1] + memo[steps - 2]
}

func climbStairs(n int) int {
    memo := make(map[int]int)
    return find(n, memo)
}