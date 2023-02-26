from sqlalchemy import Column, Integer, String,Date
from database import Base


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    product_name = Column(String(256))
    product_price= Column(Integer)
    product_exipire_date= Column(String(256))