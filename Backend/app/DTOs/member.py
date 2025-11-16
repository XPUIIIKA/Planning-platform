from pydantic import BaseModel, EmailStr

class MemberShortOut(BaseModel):
    id: int
    name: str
    role: str