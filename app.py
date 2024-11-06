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

basedata = [
    Order(number=1, startDate="2021-01-02", device="Чайник", problemType="технический", description="не кипятит", client="Чайников Чай Чаевич", status="в работе")
]

app = fastapi.FastAPI()

@app.get('/orders')
def orders():
    return basedata

@app.post('/order/create')
def create_order(order: Order):
    basedata.append(order)
    return basedata