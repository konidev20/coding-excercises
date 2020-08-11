class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index1 = {}
        index2 = {}

        for num in nums1:
            if num not in index1:
                index1[num] = 0
            index1[num] += 1

        for num in nums2:
            if num not in index2:
                index2[num] = 0
            index2[num] += 1

        union = set(nums1 + nums2)

        intersection = []

        for num in union:
            if num in index1 and num in index2:
                if index1[num] == index2[num]:
                    count = index1[num]
                else:
                    count = min(index1[num], index2[num])
                intersection = intersection + list([num] * count)

        print(union)
        return intersection
