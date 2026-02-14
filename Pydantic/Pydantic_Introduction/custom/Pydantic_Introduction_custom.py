import requests
from pydantic import BaseModel, field_validator
import uuid
from datetime import date, datetime, timedelta

url = (
    "https://raw.githubusercontent.com/haddoumounir/"
    "data/refs/heads/main/data/data-00.json"
)

data = requests.get(url)
data = data.json()

# print(data)


class Employee(BaseModel):
    employee_id: uuid.UUID
    full_name: str
    hire_date: date
    salary: float
    position: str
    team: str | None
    is_active: bool

    @field_validator("hire_date")
    def validator_hire_date(cls, value):
        three = datetime.now() - timedelta(3 * 365)
        three = three.date()
        if value > three:
            raise ValueError("you need to work more then 3 years")
        return value

    @field_validator("salary")
    def validator_salary(cls, value):
        base_salary = 55000
        if value < base_salary:
            raise ValueError(f"you can't work with less then {base_salary}\n")
        if value > base_salary:
            print("you are good on interview mate !")
        return value


for employee in data:
    model = Employee(**employee)
    print(model)
