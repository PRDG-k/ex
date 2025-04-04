class Person:
    __ub_hp = 100
    __lb_hp = 1

    def __init__(self, name, hp):
        self.__name = name
        self.__hp = hp

    @property
    def name(self):
        return self.__name
    
    @property
    def hp(self):
        return self.__hp
    
    @hp.setter
    def hp(self, hp):
        if 1 <= hp and hp <= 100:
            self.__hp = hp
        elif hp < 0:
            self.__hp = Person.__lb_hp
        else:
            self.__hp = Person.__ub_hp

    def workout(self, hour):
        self.hp += hour
        print(f"{hour}시간 운동하다")

    def drink(self, count):
        self.hp -= count
        print(f"술을 {count}잔 마시다")

    def __str__(self):
        return f"{self.name} - hp: {self.hp}"
    
p1 = Person("나몸짱", 999)
p2 = Person("나약해", 10)

p1.workout(5)
p1.drink(2)
print(p1)
print("=" * 20)
p2.workout(1)
p2.drink(12)
print(p2)