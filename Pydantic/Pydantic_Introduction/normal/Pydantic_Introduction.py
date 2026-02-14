import requests
from pydantic import BaseModel, validator
import uuid
from datetime import date, datetime, timedelta
from DepartmentEnum import DepartmentEnum

# Life Sciences
# Science and Engineering
# Life Sciences
# Arts and Humanities


url = (
    "https://raw.githubusercontent.com/bugbytes-io/"
    "datasets/refs/heads/master/students_v1.json"
)

data = requests.get(url)
data = data.json()
# print(data)


class Student(BaseModel):
    id: uuid.UUID
    name: str
    date_of_birth: date
    GPA: float
    course: str | None
    department: DepartmentEnum
    fees_paid: bool

    # !validator is deprecated ! use field_validator
    @validator("date_of_birth")
    def validator_data_of_birth(cls, value):
        valid_age = datetime.now() - timedelta(40 * 365)
        valid_age = valid_age.date()
        print(value)
        if value < valid_age:
            raise ValueError("you are to big to be student!")

    @validator("GPA")
    def validator_gpa(cls, value):
        min, max = 1, 5
        if value > min and value < max:
            print("good work")
            return value
        if value < min or value > max:
            raise ValueError(f"there is problem with your GPA: {value}")


for student in data:
    model = Student(**student)
    print(model)
