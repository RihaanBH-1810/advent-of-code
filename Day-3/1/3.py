file = open("./input.txt")
f = file.readlines()
list_lines = []

blacklist = [".", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
num_list = [ "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

part_numbers = []

for line in f:
    list_lines.append(list(line))



for i, line in enumerate(list_lines):
    for j, ele in enumerate(line):
        if ele in num_list:
            if i == 0 and j == 0:
                if (list_lines[i][j+1] not in blacklist) or (list_lines[i+1][j] not in blacklist) or (list_lines[i+1][j+1] not in blacklist):
                    part_numbers.append(int(ele))
            elif j == 0 and i != 0 and i != (len(list_lines)-1):
                if (list_lines[i][j+1] not in blacklist) or (list_lines[i-1][j] not in blacklist) or (list_lines[i-1][j+1] not in blacklist) or (list_lines[i+1][j] not in blacklist) or (list_lines[i+1][j+1] not in blacklist):
                    part_numbers.append(int(ele))
            elif j == 0 and i == (len(list_lines)-1):
                if (list_lines[i-1][j] not in blacklist) or (list_lines[i-1][j+1] not in blacklist) or (list_lines[i][j+1] not in blacklist):
                    part_numbers.append(int(ele))
            elif j != 0 and i == (len(list_lines)-1) and j != (len(line)-1):
                if (list_lines[i-1][j] not in blacklist) or (list_lines[i-1][j+1] not in blacklist) or (list_lines[i][j+1] not in blacklist) or (list_lines[i-1][j-1] not in blacklist)or (list_lines[i][j-1] not in blacklist):
                    part_numbers.append(int(ele))
            elif j == (len(line)-1) and i == (len(list_lines)-1):
                if (list_lines[i-1][j] not in blacklist) or (list_lines[i-1][j-1] not in blacklist) or (list_lines[i][j-1] not in blacklist):
                    part_numbers.append(int(ele))
            elif j == (len(line)-1) and i != (len(list_lines)-1) and i!= 0:
                if (list_lines[i][j-1] not in blacklist) or (list_lines[i-1][j] not in blacklist) or (list_lines[i-1][j-1] not in blacklist) or (list_lines[i+1][j] not in blacklist) or (list_lines[i+1][j-1] not in blacklist):
                    part_numbers.append(int(ele))
            elif i == 0 and j == (len(line)-1):
                if (list_lines[i][j-1] not in blacklist) or (list_lines[i+1][j] not in blacklist) or (list_lines[i+1][j-1] not in blacklist):
                    part_numbers.append(int(ele))     
            elif j != 0 and i == 0 and j != (len(line)-1):
                if (list_lines[i+1][j] not in blacklist) or (list_lines[i+1][j+1] not in blacklist) or (list_lines[i][j+1] not in blacklist) or (list_lines[i+1][j-1] not in blacklist)or (list_lines[i][j-1] not in blacklist):
                    part_numbers.append(int(ele))
            else:
                if (list_lines[i+1][j] not in blacklist) or (list_lines[i+1][j+1] not in blacklist) or (list_lines[i][j+1] not in blacklist) or (list_lines[i+1][j-1] not in blacklist)or (list_lines[i][j-1] not in blacklist) or (list_lines[i-1][j] not in blacklist) or (list_lines[i-1][j+1] not in blacklist) or (list_lines[i][j+1] not in blacklist) or (list_lines[i-1][j-1] not in blacklist) or (list_lines[i][j-1] not in blacklist):
                    part_numbers.append(int(ele))

print(part_numbers)
for num in part_numbers:
    
        

            

