from pydantic import BaseModel


class UsersDetails(BaseModel):
    email:str
    first_name:str
    last_name:str