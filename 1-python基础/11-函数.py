# 先声明再调用
# #表示注释 ''''''表示文档字符串，用来描述函数的作用
def greet_user():
    '''打印Hello'''
    print('Hello')
greet_user()
def haha(name):
    print(f"{name},haha")
haha('jeese')
print('----------------------------------------------------')

# 位置实参与关键字实参
def pet(pet_type, pet_name):
    """显示宠物信息"""
    print(f'我有一只{pet_type}, 他叫{pet_name}')
# 位置实参，参数位置不能乱
pet('🐱', '老王')
# 关键字实参
pet(pet_type="🐶", pet_name="老张")
# 定义函数实参默认值
def pet_info(pet_name, pet_type="🐶"):
    print(f'我有一只{pet_type}, 他叫{pet_name}')
pet_info(pet_name="老李")
print('----------------------------------------------------')

# 返回值
def format_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name
name = format_name('老', '王')
print(name)
print('----------------------------------------------------')

# 任意数量的实参，*toppings是一个名为toppings的空元组,**是创建一个名为user_info的空字典
def make_pizza(*toppings):
    print(toppings)
make_pizza('mushrooms', 'green peppers', 'extra cheese')
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
print(build_profile('albert', 'eistein', location='princeton', field='physics'))
print('----------------------------------------------------')

# 模块是拓展名为.py的文件，保存一个pizza.py并存入以下代码
def make_pizza_module(size, *toppings):
    print(f"用以下配料制作一个{size}英寸的披萨")
    for topping in toppings:
        print(f"-{topping}")
# 在其他.py文件中先 import pizza，然后使用pizza.make_pizza_module可使用模块内函数
# 导入特定函数 from pizza import make_pizza_module，使用直接make_pizza_module
# as给函数起别名，from pizza import make_pizza_module as mpm，使用mpm方法即可
# as同样可以给模块起别名，import pizza as p，使用p.make_pizza_module