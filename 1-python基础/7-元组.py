# 列表是可变的，元组是不可变的
# 定义只包含一个元素的元组，必须在这个元素后面加上逗号
dimensions = (200, 50)
print(dimensions)
print(dimensions[0])
number = (3, )
print(number)
# 元组也可以通过for循环遍历其中的值