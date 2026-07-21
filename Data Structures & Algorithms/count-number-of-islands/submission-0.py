class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    islands += 1
                    self.findIsland(grid, row, col)
        return islands
                
    def findIsland(self, grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return 
        if grid[row][col] == "1":
            grid[row][col] = "0"
            self.findIsland(grid, row + 1, col)
            self.findIsland(grid, row - 1, col)
            self.findIsland(grid, row, col + 1)
            self.findIsland(grid, row, col - 1)
        

        