# and 一假即假
# or 一真即真
cars = ['toyota', 'audi', 'bmw', 'benz']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print('------------------------------------------')

# 可以通过str in list来检查列表中是否有某个值
# 可以通过str not in list来检查列表中是否不包含某个值
print('subaru' in cars)