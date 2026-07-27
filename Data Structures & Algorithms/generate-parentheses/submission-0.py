class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        temp = []

        def bt(open_count, close_count):
            if len(temp) == 2 * n:
                ans.append("".join(temp))
                return

            if open_count < n:
                temp.append("(")
                bt(open_count + 1, close_count)
                temp.pop()

            if close_count < open_count:
                temp.append(")")
                bt(open_count, close_count + 1)
                temp.pop()

        bt(0, 0)
        return ans