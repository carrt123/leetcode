# author:Carrt
# date:2024-03-23

class Solution:
    def reverseWords(self, s: str):
        s = s.strip()
        s = s.split()[::-1]
        return ' '.join(s)
