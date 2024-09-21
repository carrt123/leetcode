
# author:Carrt
# date:2024-03-23


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = [''] * numRows
        index, step = 0, 1
        for char in s:
            res[index] += char
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return ''.join(res)
