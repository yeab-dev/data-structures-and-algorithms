def search(nums, item):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + high // 2
        guess = nums[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
