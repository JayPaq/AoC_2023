matching_chars = ['1','2','3','4','5','6','7','8','9']
matching_words = ['one','two','three','four','five','six','seven','eight','nine']

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
            while line.find(digit, line_start) != -1:
                idx = line.index(digit, line_start)
                nums.append(idx)
                line_start = idx+1
    
    # if len(nums) == 1:
    #     nums.append(nums[0])
    #two_digits.append(int(line[min(nums)]+line[max(nums)]))
                
    numwords = []
    numwords_idx = []
    for word in matching_words:
        if line.find(word) != -1:
            idx = line.index(word)
            numwords.append(matching_words.index(word))
            numwords_idx.append(idx)
            line_start = idx+len(word)
            while line.find(word, line_start) != -1:
                idx = line.index(word, line_start)
                numwords.append(matching_words.index(word))
                numwords_idx.append(idx)
                line_start = idx+1
            
                
    # if len(numwords) == 1:
    #     numwords.append(numwords[0])
    # two_digits.append(int(matching_chars[numwords[numwords_idx.index(min(numwords_idx))]]+matching_chars[numwords[numwords_idx.index(max(numwords_idx))]]))        
    
    if len(nums) == 0:
        first_digit = matching_chars[numwords[numwords_idx.index(min(numwords_idx))]]
        second_digit = matching_chars[numwords[numwords_idx.index(max(numwords_idx))]]
    elif len(numwords_idx) == 0:
        first_digit = line[min(nums)]
        second_digit = line[max(nums)]
    else:
        if min(nums) < min(numwords_idx):
            first_digit = line[min(nums)]
        else:
            first_digit = matching_chars[numwords[numwords_idx.index(min(numwords_idx))]]
        if max(nums) > max(numwords_idx):
            second_digit = line[max(nums)]
        else:
            second_digit = matching_chars[numwords[numwords_idx.index(max(numwords_idx))]]
        
    two_digits.append(int(first_digit+second_digit))

        
answer = sum(two_digits)
