class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        num = len(nums)
        if num == 0:
            return []
        if num == 1:
            return [str(nums[0])]

        start = nums[0]
        end = ""
        output = []
        for i in range(num - 1):
            if (nums[i] + 1) != nums[i + 1]:
                end = nums[i]
                if start ==  end:
                    output.append(str(end))
                else:
                    output.append(f'{start}->{end}')
                start = nums[i + 1]
            if i == (num - 2):
                end = nums[num - 1]
                if start >= end:
                    output.append(str(start))
                else:
                    output.append(f'{start}->{end}')

        return output