public class Solution {
    private void SwapAroundDiagonal(int[][] matrix)
    {
        int row = 0;
        while (row < matrix.Length)
        {
            int i = row;
            while (i < matrix.Length)
            {
                int temp = matrix[i][row];
                matrix[i][row] = matrix[row][i];
                matrix[row][i] = temp;
                i++;
            }
            
            row++;
        }
    }
    
    private void SwapColumns(int[][] matrix)
    {
        int left = 0;
        int right = matrix.Length - 1;
        while (left < right)
        {
            for (int row = 0; row < matrix.Length; row++)
            {
                int temp = matrix[row][right];
                matrix[row][right] = matrix[row][left];
                matrix[row][left] = temp;
            }
            
            left++;
            right--;
        }
    }
    
    public void Rotate(int[][] matrix)
    {
        SwapAroundDiagonal(matrix);
        SwapColumns(matrix);
    }
}