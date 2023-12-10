file =  open("./input.txt", "r")

f = file.readlines()
id_sum = 0

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
    
    red_sum  = max(red_list)

    blue_sum = max(blue_list)

    green_sum = max(green_list)

    if red_sum > 12 or green_sum > 13 or blue_sum > 14:
        pass
    else:
        id_sum += (index+1)

    
print(id_sum)  
              

