def imageSmoother(self, img):
    # Return the average of the position we are viewing and its surrounding squares
    row, col = len(img), len(img[0])
    output = [[r for r in rows] for rows in img]
    for r in range(0, row):
        for c in range(0, col):
            count = 1
            # Check the row above
            if r-1 >= 0:
                output[r][c]+=img[r-1][c]
                count+=1
                if c-1 >= 0:
                    output[r][c]+=img[r-1][c-1]
                    count+=1
                if c+1 < col:
                    output[r][c]+=img[r-1][c+1]
                    count+=1
            # Check the row below
            if r+1 < row:
                output[r][c]+=img[r+1][c]
                count+=1
                if c-1 >= 0:
                    output[r][c]+=img[r+1][c-1]
                    count+=1
                if c+1 < col:
                    output[r][c]+=img[r+1][c+1]
                    count+=1
            # Check the current row
            if c-1 >= 0:
                output[r][c]+=img[r][c-1]
                count+=1
            if c+1 < col:
                output[r][c]+=img[r][c+1]
                count+=1
            output[r][c] /= count
# Return a new r*c list, using the average of the position we are viewing
    return output