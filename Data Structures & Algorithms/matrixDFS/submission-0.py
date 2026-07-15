class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])

        def helper(grid: List[List[int]], r: int, c: int, visit: set) -> List:
            if (min(r,c) < 0 or r == row or c == col or (r,c) in visit or grid[r][c] == 1):
                return 0
            if r == row - 1 and c == col -1:
                return 1
            visit.add((r,c))

            count = 0 
            count += helper(grid, r+1, c, visit)
            count += helper(grid, r-1, c, visit)
            count += helper(grid, r, c+1, visit)
            count += helper(grid, r, c-1, visit)

            visit.remove((r,c))

            return count

        return helper(grid, 0, 0, set())
        