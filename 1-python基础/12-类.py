# 类名大写
# 使用类名创建实例时，python会自动调用__init__方法
class Dog:
    '''创建一个🐶类'''
    def __init__(self, name, age):
        '''初始化属性，姓名和年龄'''
        self.name = name
        self.age = age

    def sit(self):
        '''🐶蹲下的动作'''
        print(f"{self.name}现在蹲下了")

    def roll_over(self):
        '''🐶打滚的动作'''
        print(f"{self.name}正在打滚")
my_dog = Dog('阿拉斯加', 5)
print(f"我的狗是{my_dog.name}，它{my_dog.age}岁了")
my_dog.sit()
my_dog.roll_over()
print('------------------------------------------------------')

# 给属性指定默认值
class Car:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.odometer = 0

    def get_name(self):
        print(f'{self.year}产的{self.name}')

    def read_odometer(self):
        print(f"这辆车跑了{self.odometer}公里")

    def update_odometer(self, mileage):
        self.odometer = mileage

    def increment_odometer(self, miles):
        self.odometer += miles
my_car = Car('奥迪', 2021)
my_car.get_name()
my_car.read_odometer()
print('------------------------------------------------------')

# 修改属性的值
# 1.直接修改
my_car.odometer = 10
my_car.read_odometer()
# 2.通过方法修改，给汽车类添加一个update_odometer方法
my_car.update_odometer(11)
my_car.read_odometer()
# 3.通过方法对属性值递增，给汽车类添加一个increment_odometer方法
my_car.increment_odometer(4)
my_car.read_odometer()
print('------------------------------------------------------')

# 继承，子类会获得父类所有的属性和方法
class ElectricCar(Car):
    def __init__(self, name, year):
        """初始化父类的属性"""
        super().__init__(name, year)
        self.battery_size = 100

    def describe_battery(self):
        info = f"{self.year}年产的{self.name}电池容量{self.battery_size}千瓦时"
        return info
my_tesla = ElectricCar('tesla', 2020)
my_tesla.get_name()
print(my_tesla.describe_battery())
# 子类中又一个方法与父类方法同名，子类的实例调用该方法是会忽略父类中的这个方法，称为重写父类的方法
print('------------------------------------------------------')

# 导入类
# 将Car类放在car.py文件中，然后使用from car import Car即可引入并使用，导入多个类用，隔开
# car.py中包含多个类，使用import car可以导入整个模块，使用car.Car使用
# 别名同函数模块，使用as