matching_chars = ['1','2','3','4','5','6','7','8','9']

text_path = r"C:\Users\Jay\Desktop\input.txt"

input = open(text_path, "r")
two_digits = []
for line in input:
    nums = []
    for digit in matching_chars:
        if line.find(digit) != -1:
            idx = line.index(digit)
            nums.append(idx)
            line_start = idx+1
            line_end = -1
            while line.find(digit, line_start, line_end) != -1:
                idx = line.index(digit, line_start, line_end)
                nums.append(idx)
                line_start = idx+1

    if len(nums) == 1:
        nums.append(nums[0])
    two_digits.append(int(line[min(nums)]+line[max(nums)]))
        
answer = sum(two_digits)
