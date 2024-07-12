n, m = map(int, input().split())
nums = [i + 1 for i in range(n)]
buff = 0
maximum = nums[-1]
answer = ''

if n >= m >= 2:
    while nums[-1] != nums[0]:
        answer += str(nums[buff])
        buff += m - 1
        while len(nums[buff::]) < m:
            num = nums[len(nums)-1]
            if num >= maximum:
                num = 1
                nums.append(num)
            else:
                num += 1
                nums.append(num)

    answer += str(nums[buff])
    print(answer)
else:
    print(False)

