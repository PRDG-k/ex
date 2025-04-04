class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def update_quantity(self, amount):
        self.quantity += amount

    def display_info(self):
        print(f"상품명: {self.name}")
        print(f"가격: {self.price}원")
        print(f"재고: {self.quantity}개")


class Electronic(Product):
    def __init__(self, name, price, quantity, warranty_period = 12):
        super().__init__(name, price, quantity)
        self.warranty_period = warranty_period

    def extend_warranty(self, months):
        self.warranty_period += months
        print(f"보증기간이 {months} 연장되었습니다. 현재 보증기간: {self.warranty_period}개월")

    def display_info(self):
        super().display_info()
        print(f"보증 기간: {self.warranty_period}개월")


class Food(Product):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date

    def is_expired(self, current_date):
        if self.expiration_date >= current_date:
            print(f"{self.name}은 유통기한이 지나지 않았습니다.")
        else:
            print(f"{self.name}은 유통기한이 지났습니다.")

    def display_info(self, current_date):
        self.is_expired(current_date)
        super().display_info()

tv = Electronic("스마트 TV", 1500000, 5, 24)
tv.display_info()
tv.extend_warranty(12)
tv.display_info()

apple = Food("사과", 3000, 50, "2025-04-04")
apple.is_expired("2025-04-04")
apple.display_info("2025-04-05")