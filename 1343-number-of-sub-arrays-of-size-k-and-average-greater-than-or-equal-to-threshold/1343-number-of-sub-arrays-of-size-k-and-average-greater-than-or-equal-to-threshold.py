class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sol = 0
        l = 0
        r = k-1
        run_sum = sum(arr[0:k-1])
        while r < len(arr):
            run_sum += arr[r]
            if run_sum / k >= threshold:
                sol += 1
            run_sum -= arr[l]
            l += 1
            r += 1
        
        return sol