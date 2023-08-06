from pydantic import BaseModel


class Student(BaseModel):
    name: str
    email: str
    job: str
    company: str

class UpdateStudent(BaseModel):
    student_id: str
    name: str
    email: str
    job: str
    company: str