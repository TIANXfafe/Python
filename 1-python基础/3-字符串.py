# 在python中，用引号括起来的都是字符串，可以是单引号也可以是双引号
message1 = "这是一个字符串。"
message2 = '这也是一个字符串。'
print(message1)
print(message2)

# 字符串的方法
# title() 将每个单词首字母改为大写
# upper() 将所有字母改为大写
# lower() 将所有字母改为小写
message3 = "i loVE you"
print(message3.title())
print(message3.upper())
print(message3.lower())

# 在字符串中使用变量
first_word = "love"
last_word = "you"
# 3.6及以后版本才可以使用
full_word = f"I {first_word} {last_word} so much"
# 3.5及以前版本可以使用
full_word2 = "I {} {} so much".format(first_word, last_word)
print(full_word)
print(full_word2)

# 转义字符 \t制表符 \n换行符
print("\tpython")
print("JavaScript\nC\nJava\nPython")

# 删除字符串中的空白
# rstrip() 删除字符串右侧空白
# lstrip() 删除字符串左侧空白
# strip() 删除字符串两侧空白
word1 = "python "
word2 = " python"
word3 = " python "
print(word1)
print(word1.rstrip())
print(word2)
print(word2.lstrip())
print(word3)
print(word3.strip())

# 检查一个字符串中是否包含另一个字符串
day = "0202"
time = "4185964198419810202"
if day in time:
    print('存在')
else:
    print('不存在')