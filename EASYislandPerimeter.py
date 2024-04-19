class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row=len(grid)
        column=len(grid[0])
        print(row ,column)
        perimeter=0
        i=0
        j=0
        if column==1 and row==1:
            return 4
        if row==1:
            count=0
            for elem in grid[0]:
                if elem==1:
                    count+=1
            perimeter=4
            while i<count-1:
                perimeter+=2
                i+=1

            return perimeter

        if column==1:
            count=0
            for elem in grid:
                if elem[0]==1:
                    count+=1
            perimeter=4
            while i<count-1:
                perimeter+=2
                i+=1

            return perimeter

        while i<row:
            while j<column:
                if grid[i][j]==1:
                    if i==0:
                        perimeter+=1
                        if grid[i+1][j]==0:
                            perimeter+=1
                        if j==0 or j!=column-1:
                            if j==0:
                                perimeter+=1
                            if grid[i][j+1]==0:
                                perimeter+=1
                        if j==column-1 or j!=0:
                            if j==column-1:
                                perimeter+=1
                            if grid[i][j-1]==0:
                                perimeter+=1
                    elif i==row-1:
                        perimeter+=1
                        if grid[i-1][j]==0:
                            perimeter+=1
                        if j==0 or j!=column-1:
                            if j==0:
                                perimeter+=1
                            if grid[i][j+1]==0:
                                perimeter+=1
                        if j==column-1 or j!=0:
                            if j==column-1:
                                perimeter+=1
                            if grid[i][j-1]==0:
                                perimeter+=1
                    else:
                        if j==0 or j==column-1:
                            perimeter+=1
                        if grid[i-1][j]==0:
                            perimeter+=1
                        if grid[i+1][j]==0:
                            perimeter+=1
                        if j<column-1 and grid[i][j+1]==0:
                            perimeter+=1
                        if j>0 and grid[i][j-1]==0 :
                            perimeter+=1
                j+=1
            print(grid[i],perimeter)
            j=0
            i+=1

        return perimeter
