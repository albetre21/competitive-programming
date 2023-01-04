class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        row, col = 0, 0
        level = 0
        ans = []
        length = len(matrix) * len(matrix[0])
        
        while len(ans) < length:
            print(ans)
            
            while col < len(matrix[0]) - level and len(ans) < length:
                ans.append(matrix[row][col])
                col += 1
            col -= 1
            row += 1
            
            while(row < len(matrix) - level) and len(ans) < length:
                ans.append(matrix[row][col])
                row += 1
            row -= 1
            col -= 1
            
            while(col >= level) and len(ans) < length:
                ans.append(matrix[row][col])
                col -= 1
            col += 1
            row -= 1
            while row > level and len(ans) < length:
                ans.append(matrix[row][col])
                row -= 1
            row += 1
            col += 1
            level += 1
            
        return ans