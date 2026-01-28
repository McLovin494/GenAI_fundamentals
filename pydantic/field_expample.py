from pydantic import BaseModel, Field
from typing import List, Dict, Optional


class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,  # ...indicates requried field
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples="Arion Dutta",
    )
    department: Optional[str] = "General"
    salary: float = Field(..., ge=10000)


# like ge,gt,le,lt,regex
