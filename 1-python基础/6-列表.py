# 列表由一系列按特定顺序排列的元素组成
# 通过索引可以访问列表元素，索引从0开始,最后一个元素索引为-1
cars = ['奔驰', '宝马', '奥迪']
print(cars)
print(cars[1].upper())
print(cars[-1].title())
print(f"我的第一辆车是一辆{cars[0].title()}")
print("----------------------------------------------------------------")

# 通过索引可以直接修改指定元素的值
cars[0] = "法拉利"
print(cars)
print("----------------------------------------------------------------")

# 在列表中添加元素
# append 在列表末尾添加元素
# insert 在任意位置添加元素
cars.append('兰博基尼')
print(cars)
cars.insert(1, '柯尼赛格')
print(cars)
print("----------------------------------------------------------------")

# 在列表中删除元素
# del 删除指定索引的元素
# pop 删除列表末尾的元素或删除指定索引的元素，且能够直接使用
# remove 删除列表哪的指定元素，且能够直接使用
del cars[1]
print(cars)
popped_cars = cars.pop()
print(cars)
print(popped_cars)
cars.pop(1)
print(cars)
cars.remove('法拉利')
print(cars)
print("----------------------------------------------------------------")

# 列表永久排序sort()
carList = ['toyota', 'benz', 'bmw', 'audi']
print(carList)
carList.sort()
print(carList)
# 倒序排序
carList.sort(reverse=True)
print(carList)
print("----------------------------------------------------------------")

# 列表临时排序sorted()
carList = ['toyota', 'benz', 'bmw', 'audi']
print(carList)
print(sorted(carList))
print(sorted(carList, reverse=True))
print(carList)
print("----------------------------------------------------------------")

# 列表反转
cars = ['toyota', 'benz', 'bmw', 'audi']
print(cars)
cars.reverse()
print(cars)
print("----------------------------------------------------------------")

# 获取列表长度
cars = ['toyota', 'benz', 'bmw', 'audi']
print(len(cars))
print("----------------------------------------------------------------")

# 遍历列表
cars = ['toyota', 'benz', 'bmw', 'audi']
for car in cars:
    print(car)
    print(f"我觉得{car.title()}不错\nj")
print("----------------------------------------------------------------")

# 创建数值列表(range左闭右开,第三个值为步长)
for number in range(1, 5):
    print(number)
numbers = list(range(1, 6))
print(numbers)
odd_numbers = list(range(1, 10, 2))
print(odd_numbers)
print("----------------------------------------------------------------")

# min 获取列表中最小值
# max 获取列表中最大值
# sum 获取列表所有值的和
numbers = list(range(1, 11))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print("----------------------------------------------------------------")

# 列表解析
squares = [value ** 2 for value in range(1, 11)]
print(squares)
print("----------------------------------------------------------------")

# 列表切片(索引左闭右开，第三个值为步长)
numbers = list(range(1, 10))
print(numbers[0 : 5])
print(numbers[: 5])
print(numbers[5:])
print(numbers[-3:])
print(numbers[0 : 5 : 2])
print("----------------------------------------------------------------")

# 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("my_foods", my_foods)
print("friend_foods", friend_foods)