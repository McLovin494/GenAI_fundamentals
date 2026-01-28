from pydantic import BaseModel, field_validator, model_validator


class User(BaseModel):
    username: str

    # just for individual fields
    @field_validator("usernae")
    def username_length(cls, v):
        if len(v) < 4:
            raise ValueError("Username must be atleast 4 characters")
        return v


class SignUpData(BaseModel):
    password: str
    confirm_password: str

    # after field validator
    @model_validator(mode="after")
    def password_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError("Passwords don't match")
        return values

    # make sure to return the value for both model valdiator and field validator
