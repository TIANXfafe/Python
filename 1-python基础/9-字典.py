# 字典是一系列键值对
person = {'name': 'tian', 'age': 5}
print(person)
print(person['name'])
print(person['age'])
person['score'] = 100   # 向字典中添加新的值
print(person)
person['age'] = 6   # 修改字典中的值
print(person)
del person['name']  # 删除键值对
print(person)
print('------------------------------------------------------------------')

# 使用get访问值可以在指定键不存在时返回一个默认值，而使用方括号如果不存在会报错
# 如果没有指定第二个参数，且指定的键不存在，返回None
height = person.get('height', 'No height value assigned')
print(height)
print('------------------------------------------------------------------')

# 遍历字典
user = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}
# 遍历字典中键和值
for key, value in user.items():
    print(f"Key: {key}")
    print(f"Value: {value}\n")
# 遍历字典中所有的键
# for key in user: 与下一种写法等价
# keys()返回一个列表，所以可以查询字典中是否存在某个属性    if 'xxx' in user.keys():
for key in user.keys():
    print(key.title())
# 按特定顺序遍历字典中所有键
for key in sorted(user.keys()):
    print(key)
# 遍历字典中所有的值
for value in user.values():
    print(value.title())
# 遍历字典中的所有的值并去重，使用集合set
for value in set(user.values()):
    print(f"{value}, 未重复")