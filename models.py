from pydantic import BaseModel, Field

# This class defines how user data should look
class User(BaseModel):
    username: str = Field(min_length=2)  # name must be at least 2 characters
    password: str
    age: int = Field(gt=0)  # age must be greater than 0