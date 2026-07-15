# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge_sort(self, arr, s, e):
        if e - s + 1 <= 1:
            return arr
        
        m = (s + e) // 2

        self.merge_sort(arr, s, m)

        self.merge_sort(arr, m+1, e)

        self.merge(arr, s, m, e)

        return arr
    
    def merge(self, arr, s, m, e):
        left = arr[s: m+1]
        right = arr[m+1: e+1]

        i = 0 #index for left
        j = 0 #index for right
        k = s #index for main arr

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

            
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.merge_sort(pairs, 0, len(pairs))
