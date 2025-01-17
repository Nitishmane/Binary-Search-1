# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        low = 0
        high = 1
        while (reader.get(high) < target):
            low = high + 1
            high = high * 2

        return self.binarysearch(reader, low, high, target)

    def binarysearch(self, reader, low, high, target):

        while (low <= high):
            mid = low + (high - low) // 2
            mid_element = reader.get(mid)
            if mid_element == target:
                return mid
            elif target < mid_element:
                high = mid - 1
            else:
                low = mid + 1
        return -1