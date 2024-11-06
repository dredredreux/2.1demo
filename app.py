import datetime
import fastapi
import pydantic

class Order(pydantic.BaseModel):
    number: int
    startDate: datetime.date
    device: str
    problemType: str
    description: str
    client: str
    status: str

basedata = []