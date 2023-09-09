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
    for j in range(characters.count(modify[i][0])):
        location = characters.index(modify[i][0],fd+1)
        characters[location]=modify[i][2]
        fd = location

output = "".join(characters)
with open("characters.txt","w",encoding='utf-8') as file:
    file.write(output)