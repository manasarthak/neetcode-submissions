class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mp = {}
        for course, pre in prerequisites:
            mp.setdefault(course, []).append(pre)

        on_stack = set()   # gray: on the current path
        done = set()       # black: fully processed
        ans = []

        def dfs(i):
            if i in on_stack:
                return False       # back edge -> cycle
            if i in done:
                return True        # already emitted, skip
            on_stack.add(i)
            for pre in mp.get(i, []):
                if not dfs(pre):
                    return False
            on_stack.remove(i)
            done.add(i)
            ans.append(i)          # post-order: after all prereqs
            return True

        for j in range(numCourses):
            if not dfs(j):
                return []
        return ans