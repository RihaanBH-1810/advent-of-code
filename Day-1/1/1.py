file  = open ("input.txt", "r")
sum = 0
for i in range(1000):
    numbers = []
    line = file.readline()
    for ch in line:
        if ch >= "0" and ch <= "9":
            numbers.append(int(ch))
    if len(numbers) == 1:
        sum += (numbers[0]*10+numbers[0])
    if len(numbers) >= 2:
        sum += (numbers[0]*10+numbers[-1])
print(sum)        
