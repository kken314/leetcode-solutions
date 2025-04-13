class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashtable = {}
        for num in arr:
            if num in hashtable:
                hashtable[num] += 1
            else:
                hashtable[num] = 1
        
        occ = list(hashtable.values())
        return len(occ) == len(set(occ))