class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        most_freq = count.most_common(k) #get the k most common numbers 

        result = []

        for num, freq in most_freq:
            result.append(num)
        return result

        