
# Leetcode mock interview - https://leetcode.com/problems/flood-fill/


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        m, n = len(image), len(image[0])
        scolor = image[sr][sc]

        def recurse_pixel(sr, sc):

            if sr < 0 or sr >= m or sc < 0 or sc >= n:
                return
            if image[sr][sc] == newColor or image[sr][sc] != scolor:
                return

            image[sr][sc] = newColor

            recurse_pixel(sr-1, sc)      # top
            recurse_pixel(sr, sc+1)      # right
            recurse_pixel(sr+1, sc)      # down
            recurse_pixel(sr, sc-1)      # left

        recurse_pixel(sr, sc)

        return image
