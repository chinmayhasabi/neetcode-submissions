from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            sorted_chars = sorted(word)
            key = ''.join(sorted_chars)
            groups[key].append(word)
        return list(groups.values())
       