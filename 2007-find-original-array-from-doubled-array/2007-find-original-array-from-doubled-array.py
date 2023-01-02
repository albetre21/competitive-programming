class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []

        changed.sort()
        arr1 = []
        len_arr2 = 0
        match_idx = 0
        for idx, value in enumerate(changed):       
            if len(arr1) == len_arr2:
                arr1.append(value)
                continue
            if value < arr1[match_idx] * 2:
                arr1.append(value)
            elif value == arr1[match_idx] * 2:
                len_arr2 += 1
                match_idx += 1
            else:
                return []

        return arr1 if len(arr1) == len_arr2 else []
