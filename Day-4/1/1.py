file =  open("./input.txt", "r")
line_list = file.readlines()
tot = 0
listk = []
scores = []
for i in line_list:
    listk.append(1)
for i,line in enumerate(line_list):
    pos = []
    score = 0
    line_arr = line.split()
    for wd in line_arr:
        if  ":" in wd:
            pos.append(line_arr.index(wd))
        if wd == "|":
            pos.append(line_arr.index(wd))
    
    winning_no_Llist = line_arr[pos[0]+1:pos[1]]
    no_list = line_arr[pos[1]+1:]
    
    for item in no_list:
        if item in winning_no_Llist:
            score += 1
    for j in range(i-1, i+score):
        listk[j] += 1
    scores.append(score)

for i in range(len(scores)):
    tot += (scores[i]*listk[i])
print(tot)

        


