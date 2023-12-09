file =  open("./input.txt", "r")

f = file.readlines()
power_sum = 0

for index, line in enumerate(f):
    red_sum = 0 
    blue_sum = 0
    green_sum = 0
    red_list = []
    blue_list = []
    green_list = []
    line_arr = line.split()

    for word in line_arr:
        if "red" in word or "red," in word or "red;" in word:
            red_list.append(int(line_arr[line_arr.index(word)-1]))
            line_arr.remove(word)
    for word in line_arr:
        if "blue" in word or "blue," in word or "blue;" in word:
            blue_list.append(int(line_arr[line_arr.index(word)-1]))
            line_arr.remove(word)
    for word in line_arr:
        if "green" in word or "green," in word or "green;" in word:
            green_list.append(int(line_arr[line_arr.index(word)-1]))
            line_arr.remove(word)
    
    red_max = max(red_list)

    blue_max = max(blue_list)

    green_max = max(green_list)

    power  = red_max * blue_max * green_max

    power_sum += power



    
print(power_sum)  