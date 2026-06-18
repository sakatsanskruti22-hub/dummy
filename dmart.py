class dmart:
 storename="dmart"
 def __init__(self,category,product_name,qty,price):
  self.category=category
  self.product_name=product_name
  self.qty=qty
  self.price=price

  @classmethod
  def display_stores_details(cls):
   return f"store name  -->{cls.storename}"
  
  def common_feature(self):
   return f"category:{self.category}\nproduct_name:{self.product_name}\nqty:{self.qty}\nprice:{self.price}"

