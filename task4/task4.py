import argparse

nums = []
parser = argparse.ArgumentParser()
parser.add_argument('nums_file', type=str)
args = parser.parse_args()
print('to use write in console: python task4.py path/to/nums.txt ')

with open(args.nums_file, 'r') as file:
    for line in file:
        nums.append(int(line.strip()))

nums.sort()
median = nums[len(nums)//2]
min_sum = sum(abs(num-median) for num in nums)
print(min_sum)