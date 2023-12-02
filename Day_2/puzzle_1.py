text_path = r"C:\Users\Jay\Desktop\input.txt"

max_amts = [12, 13, 14]
colors = ['red', 'green', 'blue']

input = open(text_path, "r")

assess_count = 0
for line in input:
    assess_flag = 0
    game = line.split(":")[0]
    game_num = game.split()[1]
    results = line.split(":")[1]
    trials = results.split(";")
    for trial in trials:
        counts = trial.split(",")
        for count in counts:
            amount = count.split()[0]
            color = count.split()[1]
            c_idx = colors.index(color)
            c_max = max_amts[c_idx]
            if int(amount) > c_max:
                assess_flag = assess_flag+1

    if assess_flag == 0:
        assess_count = assess_count + int(game_num)
