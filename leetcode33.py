class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min = 0; max = len(nums) - 1 #初始化边界
        # if target > nums[max] and target < nums[min]:
        #     return -1
        # if target == nums[min]:
        #     return min
        # if target == nums[max]:
        #     return max
        #二分法搜索
        while min <= max:
            mid = (min + max)//2
            print(min,max,mid)
            if target > nums[mid]:
                if nums[min] < nums[mid]  or target <= nums[max]: #如果target一定在右半边
                    min = mid + 1
                else:
                    max = mid - 1
            elif target < nums[mid]:
                if nums[max] > nums[mid] or target >= nums[min]:#如果target一定在左半边
                    max = mid - 1
                else:
                    min = mid + 1
            else:
                return mid
        return -1 #如果没有找到