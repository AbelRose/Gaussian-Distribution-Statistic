import numpy as np

def getDate() -> object:
    f = open("Statistic_Data.txt", "r")
    source = []
    for line in f.readlines():
        if line.startswith("ReqTime"):
            source.append(line.strip()[14:])
            nums = list(map(lambda x: int(x), source))

    print(nums)

    # 求均值
    arr_mean = np.mean(nums)
    # 求方差
    arr_var = np.var(nums)
    # 求标准差
    arr_std = np.std(nums, ddof=1)
    print("平均值为：%f" % arr_mean)
    print("方差为：%f" % arr_var)
    print("标准差为:%f" % arr_std)

    print("3σ区间:","[", (arr_mean-3 * arr_std),",",(arr_mean+3 * arr_std),"]")
    print("有99.74%的把握")
    # data = np.array(nums)
    # np.savetxt('out.txt', data, fmt="%d")  # 保存为整数
    # print(isinstance(nums[0],int))


getDate()
