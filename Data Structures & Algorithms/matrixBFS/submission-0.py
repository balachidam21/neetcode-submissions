class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])

        visit = set()
        queue = deque()

        queue.append((0,0))
        visit.add((0,0))

        length = 0

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                if r == row - 1 and c == col - 1:
                    return length

                neighbors = [[0,1], [0,-1], [-1, 0], [1, 0]]
                for dr, dc in neighbors:
                    if (min(r+dr, c+dc) < 0 or r+dr == row or c+dc == col or grid[r+dr][c+dc] == 1 or (r+dr, c+dc) in visit):
                        continue
                    
                    queue.append((r+dr, c+dc))
                    visit.add((r+dr, c+dc))

            length += 1
        return -1
                        
        