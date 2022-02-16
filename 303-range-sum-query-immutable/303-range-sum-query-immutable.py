class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sum_array = []
        running_sum = 0
        for num in nums:
            running_sum += num
            self.prefix_sum_array.append(running_sum)
        print(self.prefix_sum_array)

    def sumRange(self, left: int, right: int) -> int:
        print(self.prefix_sum_array[right], self.prefix_sum_array[left])
        return self.prefix_sum_array[right] - self.prefix_sum_array[left] + self.nums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)