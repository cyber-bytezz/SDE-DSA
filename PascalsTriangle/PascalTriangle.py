from typing import List

class Solution:
    def generate(self, numRows:int) -> List[List[int]]:

        #Place the first Row as 1 Because of Pascale Triangle
        res =[[1]]

        #Build the Number of row with -1 because we already have 1 in our row so that (numRows -1)
        for i in range(numRows - 1):

            #Need to look at the last Row so that we have used res[-1] and add left & Right side adding with 0
            temp = [0] + res[-1] + [0]

            #Clear and add the Empty Row
            row = []

            #Look at the Pair of the Number 
            for j in range(len(res[-1]) + 1):

                #Sum then and append on that row
                row.append(temp[j] + temp[j+1])
            res.append(row)
        return res