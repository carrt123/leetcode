
# 非递归
def bin_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1


#递归

def bin_search2(nums, target):
    def dfs(left, right):
        if left > right:
            return
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return dfs(mid + 1, right)
        else:
            return dfs(left, mid - 1)
    return dfs(0, len(nums) - 1)