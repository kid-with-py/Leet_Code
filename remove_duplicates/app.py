###--Remove Duplicates from Sorted Array--###

def removeDuplicates(self, nums: list[int]) -> int:
    j = 1
    for i in range(1, len(nums)):
### comparing ###        
        if nums[i] != nums[i-1]:
            nums[j] = nums[i]
            j += 1

    return j       
     
