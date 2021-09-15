import json
# open方法用来打开文件，接收一个参数，当前目录下文件的名称
# read方法用来读取文件内容
with open('pi.txt') as file_object:
    contents = file_object.read()
    for line in file_object:
        print(line)
print(contents)
print("------------------------------------------------")

# 逐行读取
# with open('pi.txt') as file_object:
#     for line in file_object:
#         print(line)

# readline方法，从文件中读取每一行并存储在一个数组中
# with open('pi.txt') as file_object:
#     lines = file_object.readline()
# for line in lines:
#     print(line)

# 写入空文件，写入非空文件
# w  写入模式
# r  读取模式，默认
# a  附加模式
# r+ 读写模式
filename = 'empty.txt'
with open(filename, 'w') as file:
    file.write("我喜欢奔驰")
with open(filename, 'a') as file2:
    file2.write("我也喜欢宝马\n")
    file2.write("我也喜欢奥迪")
print("------------------------------------------------")

# 异常
try:
    print(5 / 0)
except ZeroDivisionError:
    print('被除数不能为0')
first_num = 5
second_num = 0
try:
    answer = int(first_num) / int(second_num)
except ZeroDivisionError:
    print('被除数不能为0')
else:
    print(answer)
# split()方法可以将字符串分割为数组
print("------------------------------------------------")

# JSON，先在最上方import json
num = [2, 3, 5, 7 ,9]
filename2 = 'num.json'
with open(filename2, "w") as f:
    json.dump(num, f)
with open(filename2) as f2:
    nums = json.load(f2)
print(nums)