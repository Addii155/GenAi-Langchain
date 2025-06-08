from pydantic import BaseModel, Field
from typing import Optional
class Student(BaseModel):
    name:str
    age:Optional[int]=None

new_student={'name':"Aditya"}
s2 = Student(**new_student)
print(s2)   