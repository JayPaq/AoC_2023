text_path = r"C:\Users\Jay\Desktop\input.txt"

max_amts = [12, 13, 14]
colors = ['red', 'green', 'blue']

input = open(text_path, "r")

powers = []
for line in input:
    assess_flag = 0
    game = line.split(":")[0]
    game_num = game.split()[1]
    results = line.split(":")[1]
    trials = results.split(";")
    highest_amt = [0,0,0]
    for trial in trials:
        counts = trial.split(",")
        for count in counts:
            amount = count.split()[0]
            color = count.split()[1]
            c_idx = colors.index(color)
            if highest_amt[c_idx] < int(amount):
                highest_amt[c_idx] = int(amount) 

    powers.append(highest_amt[0]*highest_amt[1]*highest_amt[2]) 

answer = sum(powers)
