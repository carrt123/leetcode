# author:Carrt
# date:2024-03-20

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        s = s.strip()
        return len(s.split()[-1])

s = "   luffy is still joyboy"
print(Solution().lengthOfLastWord(s))
