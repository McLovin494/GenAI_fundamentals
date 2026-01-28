from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: int
    in_stock: bool = True  # default value


product_one = Product(id=1, name="Laptop", price=999.99, in_stock=False)
product_two = Product(id=2, name="Mouse", price=24.33)
product_three = Product(name="Keyboard")
# always use type annotations
# use appropiate types
# int ,float , bool
# set a sensible default
