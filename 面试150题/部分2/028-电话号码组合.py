from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.num_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        self.res = []
        self.dfs(digits, 0, '', self.res) if digits else []
        return self.res

    def dfs(self, digits: str, index: int, path: str, res: List[str]):
        if index == len(digits):
            self.res.append(path)
            return
        for c in self.num_map[digits[index]]:
            self.dfs(digits, index + 1, path + c, res)


d = '23'
s = Solution()
print(s.letterCombinations(d))
