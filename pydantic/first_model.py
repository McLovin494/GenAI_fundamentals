from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    is_active: bool


input_data = {"id": 101, "name": "Chaicode", "is_active": True}

user = User(**input_data)
print(user)

# steps
# 1. import BaseModel
# 2. Type annotations
# 3. Model initalization -->always unpack the dictionary
# 4. Automatic validation

# 5. pydantic tries its best to convert into string like 101 from '101'
