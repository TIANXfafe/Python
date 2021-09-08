# 输入的值是字符串形式
message = input("Tell me something:")
print(message)
# int()可以将输入的字符串转换为数字类型
age = input("How old are you: ")
# print(age >= 18)
print(int(age) >= 18)
print('------------------------------------------------')

# while循环
currentNum = 1
while currentNum < 5:
    print(currentNum)
    currentNum += 1
# break退出循环，continue退出本次循环