import numpy as np

def getDate() -> object:
    f = open("Statistic_Data.txt", "r")
    source = []
    for line in f.readlines():
        if line.startswith("ReqTime"):
            source.append(line.strip()[14:])
            nums = list(map(lambda x: int(x), source))
    print(nums)

    # print(isinstance(nums[0],int))


getDate()
