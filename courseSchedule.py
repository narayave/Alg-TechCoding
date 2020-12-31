
# Leetocde - https://leetcode.com/problems/course-schedule


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        am = defaultdict(lambda: [])

        for i in prerequisites:
            c, r = i[0], i[1]
            am[r].append(c)

        def cycle(n, stack, seen):
            stack[n] = True
            seen[n] = True
            # print(n, stack, seen)
            for i in am[n]:
                if i not in seen and cycle(i, stack, seen):
                    return True
                elif i in stack:
                    return True
            stack.pop(n)
            return False

        seen = {}
        for n in range(numCourses):
            stack = {}
            if n not in seen and cycle(n, stack, seen):
                return False

        return True
