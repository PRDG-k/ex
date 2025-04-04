# class Employee:
#     def __init__(self, name):
#         self.serial_num= 1000# 인스턴스 변수
#         self.serial_num += 1
#         self.id = self.serial_num # idOll serial_num Md
#         self.name = name

#     def __str__(self):
#         return f"사번: {self.id}, 이름: {self.name}"
    

# kim = Employee("Kim")
# lee = Employee("Lee")

# print(kim)
# print(lee)

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age

    def __str__(self):
        return f"name: {self.name}, age: {self.age}"

p1 = Person("홍길동", 10)
print(p1)
p1.name = "홍박사"
print(p1)