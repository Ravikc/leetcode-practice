#User function Template for python3

class Solution:
    def checkAllRowsAreOne(self, M, col):
        for row in range(len(M)):
            if row != col and M[row][col] == 0:
                return False
                
        return True
        
    def checkAllColsAreZero(self, M, row):
        for col in range(len(M)):
            if M[row][col] == 1:
                return False
                
        return True
    
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        for i in range(n):
            if self.checkAllColsAreZero(M, i) and self.checkAllRowsAreOne(M, i):
                return i
                
        return -1
                
            


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends