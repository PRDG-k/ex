class Supermarket:
    total_customer = 0

    def __init__(self, location, name, product, customer):
        self.location = location
        self.name = name
        self.product = product
        self.customer = customer
        Supermarket.total_customer += customer


    def print_location(self, end = "\n"):
        print(f"위치: {self.location}", end=end)

    def change_category(self,new_product):
        self.product = new_product
    
    def show_list(self, end= "\n"):
        print(f"상품: {self.product}", end=end)

    def print_name(self, end="\n"):
        print(f"상품: {self.name}", end=end)

    def print_customer(self, end="\n"):
        print(f"고객수: {self.customer}", end=end)
    
    def enter_customer(self):
        self.customer = self.customer + 1
        Supermarket.total_customer += 1
    
    def print_total_customer(self):
        print(f"총 고객수: {Supermarket.total_customer}")

    def show_info(self):
        self.print_location(end=", ")
        self.print_name(end=", ")
        self.show_list(end=", ")
        self.print_customer(end=", ")
        self.print_total_customer()


branch1 = Supermarket(
        location="마포구 염리동",
        name="마켓온",
        product="음료",
        customer=12,
        )

branch1.print_location()
branch1.show_list()
branch1.show_info()

branch2 = Supermarket(
        location="마포구 염리동",
        name="마켓온2",
        product="음료",
        customer=12,
        )

branch1.show_info()
branch2.enter_customer()
branch2.show_info()
