#-*- coding:utf-8 -*-
import unicodedata
with open("characters.txt","r",encoding='utf-8') as file:
    characters = []
    char = file.read()
    for i in range(len(char)):
        characters.append(char[i])
with open("modify_vertical.txt","r",encoding='utf-8') as file:
    modify=file.readlines()
for i in range(0,len(modify)):
    fd = -1
    location = 0
    # if 0x4e00 > ord(modify[i][2]) or ord(modify[i][2]) > 0x9fff:
    #     continue
    for j in range(characters.count(modify[i][0])):
        location = characters.index(modify[i][0],fd+1)
        characters[location]=modify[i][2]
        fd = location

output = "".join(characters)
with open("characters.txt","w",encoding='utf-8') as file:
    file.write(output)

# l = ['.'*4 for _ in range(2)]
# print(l)#输出：['....', '....']
# print(l[0][2])#输出：.

# l[0] = list(l[0])#第一步将列表转换成字符串
# print(l)#输出：[['.', '.', '.', '.'], '....']

# l[0][2] = 'Q'#改变列表中的元素
# print(l)#输出：[['.', '.', 'Q', '.'], '....']

# l[0] = ''.join(l[0])#将列表转换成字符串
# print(l)#输出：['..Q.', '....']