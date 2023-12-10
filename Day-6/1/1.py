file = open("input.txt")
line_list = file.readlines()

time_list = line_list[0].split()
distance_list = line_list[1].split()

time_list = time_list[1:]
distance_list = distance_list[1:]

no_of_Ways = []

for i in range(len(time_list)):
    time_list[i] = int(time_list[i])
    distance_list[i] = int(distance_list[i])

for i, time in enumerate(time_list):
    ways = 0
    for x in range(time+1):
        if x*(time-x) > distance_list[i]:
            ways += 1
    no_of_Ways.append(ways)
pro = 1
for no in no_of_Ways:
    pro *= no
print(pro)

