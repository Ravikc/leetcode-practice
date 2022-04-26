#User function Template for python3

class Solution:
    def maximizeArray(self, arr1, arr2, n):
        topN = list(set(arr1 + arr2))
        topN.sort(reverse=True)
        topN = set(topN[:n])
        
        ans = []
        both = arr2 + arr1
        for num in both:
            if num in topN:
                ans.append(num)
                topN.remove(num)
                if len(topN) == 0:
                    break
        
        return ans
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input().strip())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maximizeArray(arr1, arr2, n)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1

# } Driver Code Ends