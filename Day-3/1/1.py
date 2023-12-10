
file = open("input.txt")
f = file.readlines()
list_lines = []

blacklist = [".", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
num_list = [ "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

part_numbers = []

for line in f:
    list_lines.append(list(line))

def fng(l):
    n=0
    t=1
    for i in l[::-1]:
        n=n+i*t
        t*=10
    print(n)
    return n

sum = 0
for i, line in enumerate(list_lines):
    a=0
    print("i   : ",i)
    for j, ele in enumerate(line):
        if a:
            a-=1
            continue
        if ele in num_list:
            part = None
            if i == 0 and j == 0:
                if (list_lines[i][j+1] not in blacklist) or (list_lines[i+1][j] not in blacklist) or (list_lines[i+1][j+1] not in blacklist):
                    part=int(ele)
            elif j == 0 and i != 0 and i != (len(list_lines)-1):
                if (list_lines[i][j+1] not in blacklist) or (list_lines[i-1][j] not in blacklist) or (list_lines[i-1][j+1] not in blacklist) or (list_lines[i+1][j] not in blacklist) or (list_lines[i+1][j+1] not in blacklist):
                    part=int(ele)
            elif j == 0 and i == (len(list_lines)-1):
                if (list_lines[i-1][j] not in blacklist) or (list_lines[i-1][j+1] not in blacklist) or (list_lines[i][j+1] not in blacklist):
                    part=int(ele)
            elif j != 0 and i == (len(list_lines)-1) and j != (len(line)-1):
                if (list_lines[i-1][j] not in blacklist) or (list_lines[i-1][j+1] not in blacklist) or (list_lines[i][j+1] not in blacklist) or (list_lines[i-1][j-1] not in blacklist)or (list_lines[i][j-1] not in blacklist):
                    part=int(ele)
            elif j == (len(line)-1) and i == (len(list_lines)-1):
                if (list_lines[i-1][j] not in blacklist) or (list_lines[i-1][j-1] not in blacklist) or (list_lines[i][j-1] not in blacklist):
                    part=int(ele)
            elif j == (len(line)-1) and i != (len(list_lines)-1) and i!= 0:
                if (list_lines[i][j-1] not in blacklist) or (list_lines[i-1][j] not in blacklist) or (list_lines[i-1][j-1] not in blacklist) or (list_lines[i+1][j] not in blacklist) or (list_lines[i+1][j-1] not in blacklist):
                    part=int(ele)
            elif i == 0 and j == (len(line)-1):
                if (list_lines[i][j-1] not in blacklist) or (list_lines[i+1][j] not in blacklist) or (list_lines[i+1][j-1] not in blacklist):
                    part=int(ele)     
            elif j != 0 and i == 0 and j != (len(line)-1):
                if (list_lines[i+1][j] not in blacklist) or (list_lines[i+1][j+1] not in blacklist) or (list_lines[i][j+1] not in blacklist) or (list_lines[i+1][j-1] not in blacklist)or (list_lines[i][j-1] not in blacklist):
                    part=int(ele)
            else:
                if (list_lines[i+1][j] not in blacklist) or (list_lines[i+1][j+1] not in blacklist) or (list_lines[i][j+1] not in blacklist) or (list_lines[i+1][j-1] not in blacklist)or (list_lines[i][j-1] not in blacklist) or (list_lines[i-1][j] not in blacklist) or (list_lines[i-1][j+1] not in blacklist) or (list_lines[i][j+1] not in blacklist) or (list_lines[i-1][j-1] not in blacklist) or (list_lines[i][j-1] not in blacklist):
                    part=int(ele)
            l=[]
            if part!=None:
                l.append(part)
                if str(line[j+1]) in num_list :
                    l.append(int(line[j+1]))
                    if str(line[j+2]) in num_list :
                        l.append(int(line[j+2]))
                    elif str(line[j-1]) in num_list :
                        l.insert(0,int(line[j-1]))
                else:
                    if str(line[j-1]) in num_list :
                        l.insert(0,int(line[j-1]))
                        if str(line[j-2]) in num_list:
                            l.insert(0,int(line[j-2]))
                a=len(l)-l.index(part)-1
            if l!=[]:
                sum = sum + fng(l)

print(sum)
    

            




# import re
# def splChar(l):
#     l.strip()
#     if l.isalpha() or l.isdigit() or l=='':
#         return False
#     return True


# with open('advent_input3.txt','r') as obj:
#     data = obj.readlines()
#     for i in range(len(data)):
#         data[i]=(data[i]).strip()
# for i in range(len(data)):
#     for j in range(data[i]):
#         line= data[i]
#         if splChar(line[j]):
#             if j==0: 
#                 if i==0:p([s if s.isdigit() else '' for s in [line[j+1],data[i-1][j],data[i-1][j+1]]])
#                 if i==(len(data)-1):p([s if s.isdigit() else '' for s in [line[j+1],data[i+1][j],data[i+1][j+1]]])
#                 else:p([s if s.isdigit() else '' for s in [line[j+1],data[i][]]])
#             elif j==len(line)-1:
#                 try:
#                     if 
#                 except:pass
#             else:



