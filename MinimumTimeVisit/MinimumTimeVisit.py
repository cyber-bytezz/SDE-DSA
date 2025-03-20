class Solution:
    def MinimumToVisit(self, points: List[List[int]]) -> int:

        # Need to track the Time starts from 0
        time_count = 0

        # Lets start the loop from 0 and in this why we are adding -1 is it wont go out of Bound
        for i in range(len(points) - 1):

            # Making the Current point
            x1,y1 = points[i]

            # Making the Next Point +1
            x2,y2 = points[i+1]

            # Formula 
            time = max(abs(x2-x1), abs(y2-y1))

            # Update the Time Total
            time_count += time
        
        # Return the time_count
        return time_count