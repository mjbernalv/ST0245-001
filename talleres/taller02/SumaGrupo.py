def Suma_grupo(start, nums, target):
    if (start == len(nums)):
        return target == 0
    else:
        usar = Suma_grupo(start+1, nums, target-nums[start])
        noUsar = Suma_grupo(start+1, nums, target)
        return usar or noUsar

print(Suma_grupo(0,[2, 4, 8],10))