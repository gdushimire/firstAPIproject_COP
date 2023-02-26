
from pydantic import BaseModel


class Item(BaseModel):
    product_name :str
    product_price : int
    product_exipire_date : str
