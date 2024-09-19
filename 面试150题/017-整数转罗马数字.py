# author:Carrt
# date:2024-03-20

class Solution:
    # 贪心算法
    def intToRoman(self, num: int) -> str:
        # 罗马数字的映射关系
        roman_map = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }
        res = ""
        for k, v in roman_map.items():
            while num >= k:
                num -= k
                res += v
            if num == 0:
                break
        return res


num = 10000
print(Solution().intToRoman(num))
