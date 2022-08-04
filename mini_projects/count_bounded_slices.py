

def calculate_slices(k: int, nums: list[int]) -> int:
    num_slices = 0

    # iterate through all indexes in the list
    for x in range(len(nums)):
        # each index must be compared to all other indexes either equal to or greater than itself
        for y in range(x, len(nums)):
            # print(f"X: {x} | Y: {y}")
            maxnum, minnum = 0, 0
            # if x and y are equal, use different syntax
            if x == y:
                maxnum, minnum = nums[x], nums[x]
            # the y+1 syntax won't work because it will cause an index out of bounds error
            # so we can leave the argument empty after the colon to get values up to and including the last index
            elif y == len(nums) - 1:
                maxnum, minnum = max(nums[x:]), min(nums[x:])
            # y + 1 must be used for the ending index since it's exclusive
            else:
                # determine max value
                maxnum = max(nums[x:y+1])
                # determine min value
                minnum = min(nums[x:y+1])
            # if difference between max and min is <= k
            if k >= maxnum - minnum:
                # print("IS DIFFERENCE LESS THAN K: TRUE")
                # print(f"MAX({maxnum}) - MIN({minnum}) <= {k}")
                num_slices += 1

    # if number of slices exceeds 1 billion, set num_slices to 1000000000
    if num_slices > 1000000000:
        num_slices = 1000000000
    return num_slices


if __name__ == "__main__":
    num_slices = calculate_slices(2, [3, 5, 7, 6, 3])
    print(f"Number of bounded slices: {num_slices}")