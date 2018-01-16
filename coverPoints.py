

# https://codelab.interviewbit.com/problems/reach/
# Facebook CodeLab
# From one location, you can go in 8 directions around you.
# How many steps to get from 1 point to another.
# Follow the set of points given.


class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    def coverPoints(self, X, Y):
        steps = 0
        for i in xrange(1, len(X)):
            x_sum = abs(X[i] - X[i-1])
            y_sum = abs(Y[i] - Y[i-1])
            steps += max(x_sum, y_sum)
        return steps