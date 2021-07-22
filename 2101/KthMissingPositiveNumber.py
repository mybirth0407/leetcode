class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr_ = list(range(1, arr[0]))
        for i in range(1, len(arr)):
            arr_.extend(list(range(arr[i-1] + 1, arr[i])))
            
        if k > len(arr_):
            # last extend
            return arr[-1] + k - len(arr_)
        else:
            return arr_[k-1]