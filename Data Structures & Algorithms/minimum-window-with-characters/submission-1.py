class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or not t:
            return ""

        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        have = {}
        formed = 0                 # how many chars meet their required count
        required = len(need)
        best = [float('inf'), 0, 0]  # length, left, right

        l = 0
        for r in range(len(s)):
            ch = s[r]
            have[ch] = have.get(ch, 0) + 1
            if ch in need and have[ch] == need[ch]:
                formed += 1

            while formed == required:          # window is valid, shrink
                if r - l + 1 < best[0]:
                    best = [r - l + 1, l, r]
                left_ch = s[l]
                have[left_ch] -= 1
                if left_ch in need and have[left_ch] < need[left_ch]:
                    formed -= 1
                l += 1

        length, i, j = best
        return "" if length == float('inf') else s[i:j+1]