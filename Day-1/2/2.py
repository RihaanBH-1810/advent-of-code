words = {
    "one" : 1,
    "two" :2,
    "three" :3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,
    "zero" :0
}
sum = 0 
file = open("input.txt", "r")

f_l = ["z","o", "t", "f", "s", "e","n"]
n_l = {
    "ze":["zero", 4], "on":["one", 3], "tw":["two", 3],"th":["three",5], "fo":["four", 4],"fi":["five", 4], "si":["six",3],"se":["seven", 5], "ei":["eight", 5], "ni":["nine", 4]
}
for i in range(1000):
    line = file.readline()
    numbers = []
    for pos, ch in enumerate(line):
        if(ch >= "0" and ch <= "9"):
            numbers.append(int(ch))
        else:
            if ch in f_l:
                val = line[pos:(pos+2)]
                
                if(val in n_l.keys()):
                    if(line[pos:(pos+n_l[val][1])] in words.keys()):
                        numbers.append(words[n_l[val][0]])

    print(f"{i} = {line} = {numbers}")
    if len(numbers) == 1:
        sum += (numbers[0]*10+numbers[0])
    if len(numbers) >= 2:
        sum += (numbers[0]*10+numbers[-1])
print(sum) 

    















