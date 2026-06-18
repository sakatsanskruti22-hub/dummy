from dmart import dmart
class clothes(dmart):
    def __init__(self,category,product_name,qty,price):
        super().__init__(self,category,product_name,qty,price)
        self.colour=self.colour
        self.size=size



    def display_clothes_details(self):
        print(super().display_store_details())
        print(super().common_feature())
        return f"colour:{self.colour}\nsize{self.size}"   