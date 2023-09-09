import unicodedata
# 打开输入文件和输出文件
with open("characters.txt", "r", encoding="utf-8") as fin, open("changed.txt", "w", encoding="utf-8") as fout:
    # 读取输入文件的内容
    content = fin.read()
    # 遍历每个字符和它的索引
    for i, char in enumerate(content):
        # 计算期望的Unicode值
        expected = r"\u" + hex(0x4e00 + i)[2:]
        expected = expected.encode().decode("unicode_escape")
        # 如果实际的Unicode值和期望的不一致
        if char != expected:
            # 写入输出文件，格式为：期望的汉字 空格 实际的字符 换行
            fout.write(f"{expected} {char}\n")
# 关闭文件
fin.close()
fout.close()
