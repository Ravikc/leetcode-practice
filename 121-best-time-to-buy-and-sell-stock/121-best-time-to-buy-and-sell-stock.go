func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func maxProfit(prices []int) int {
    minSoFar := prices[0]
    ans := 0
    
    for i := 1; i < len(prices); i++ {
        ans = max(ans, prices[i] - minSoFar)
        minSoFar = min(minSoFar, prices[i])
    }
    
    return ans
}