open('input.txt')
file = open("input.txt")
line_list = file.readlines()

time_list = line_list[0].split()
distance_list = line_list[1].split()

time_list = time_list[1:]
distance_list = distance_list[1:]

time = ""
distance = ""

for t in time_list:
    time += t

for d in distance_list:
    distance += d
    
time = int(time)
distance = int(distance)

no_of_ways = 0
for x in range(time+1):
    if x*(time-x) > distance:
        no_of_ways += 1

print(no_of_ways)
