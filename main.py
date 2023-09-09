#-*- coding:utf-8 -*-
from PIL import Image,ImageDraw,ImageFont
import os

with open("characters.txt", "r",encoding='utf-8') as f:
    text = f.read() 
# with open("page_00.txt", "r",encoding='utf-8') as f:
#     symbol = f.read()

def draw_full_pic(text, alpha = 0):
    image = Image.new("RGBA", (size*256,size*256), (0,0,0,alpha))
    image_draw = ImageDraw.Draw(image)
    image_draw.multiline_text((0,offset),text,fill=(256,256,256),font = font,spacing=spacing)
    return image

#初始化
size = 1
offset = 0
spacing = 2


is_change = input("是否调整默认设置?(y/n)\n>>>")
if is_change == "" or is_change == "n":
    description = '"made with tts tools by hosecoin"'
    font = ImageFont.truetype("C/Windows/Fonts/simsun.ttc", size=16)
    show = "n"


else:
    users_name = input("签下你的名字吧(选填)\n>>>")
    if users_name == "":
        description = '"made with tts tools by hosecoin"'
    else :
        description = '"made by ' + users_name + ' with tts_tool by hosecoin"'

    size = input('分辨率?(原版为1，不输默认为1)\n>>>')
    if size == "":
        size = 1
    else :
        size = int(size)

    font_path = input("使用字体的路径？(不输默认为:C\Windows\Fonts\)\n>>>")
    if font_path == "":
        font_path = "C/Windows/Fonts/"

    font = input("使用的字体？(例:simsun.ttc)(\n>>>")
    if font == "":
        font = "simsun.ttc"
    font = ImageFont.truetype(font_path + font,size=size*16)


    show = input("调整偏移量时是否显示图片?(关闭图片以继续)(y/n)(默认为n)\n>>>")
    if show == "" :
        show = "n"

    text_test = ("这是测试字欢迎到哔哩哔哩关注作者" + '\n') * 16

    #偏移量
    while True:
        image = draw_full_pic(text_test, 200)
        image.save("offset_finder.png")
        if show == "y" :
            image.show()
        
        input_offset = input("文字整体位置调整？(y/n)(默认为n)(当前偏移量：" + str(offset) + ")\n>>>")
        if input_offset == "" :
            break
        else :
            offset = int(input_offset)

    while True:
        image = draw_full_pic(text_test, 200)
        image.save("offset_finder.png")
        if show == "y" :
            image.show()
        input_spacing = input("文字行间距调整？(y/n)(默认为n)(当前行间距：" + str(spacing) + ")\n>>>")
        if input_spacing == "" :
            break
        else :
            spacing = int(input_spacing)

os.remove("./offset_finder.png")

pack_mcmeta = '''{
 "pack": {
   "pack_format": 1,
   "description":''' + description + '''
 }
}'''
my_file = './resourcepacks/pack.mcmeta'
with open(my_file, "w") as f:
        f.write(pack_mcmeta)
        
# image = draw_full_pic(text_output)
# image.save("./resourcepacks/assets/minecraft/textures/font/unicode_page_00.png")

#加入换行
text_output = ""
for n in range (78, 160):
    for j in range(1, 17):
        text_output += text[:16] + '\n'
        text = text[16:]

    num = hex(int(n))[2:] #编号
    name = "./resourcepacks/assets/minecraft/textures/font/"+"unicode_page_"+num+".png" #文件名
    
    image = draw_full_pic(text_output)
    image.save(name)
    print(num)
    text_output = ""
print("done!")