from fastapi import FastAPI, Body, Depends
import schemas
import models

from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
app = FastAPI()

# if we don't have database it will create new 1 by using engine we created
Base.metadata.create_all(engine)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@app.get("/")
def getItems(session: Session = Depends(get_session)):
    items = session.query(models.Item).all()
    return items

@app.get("/{id}")
def getItem(id: int, session: Session = Depends(get_session)):
    item = session.query(models.Item).get(id)
    return item
@app.post("/")
def addItem(item: schemas.Item, session: Session = Depends(get_session)):
    item = models.Item(product_name=item.product_name,product_price=item.product_price ,product_exipire_date=item.product_exipire_date)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item
@app.put("/{id}")
def updateItem(id: int, item: schemas.Item, session: Session = Depends(get_session)):
    itemObject = session.query(models.Item).get(id)
    itemObject.product_name = item.product_name
    itemObject.product_price = item.product_price
    itemObject.product_exipire_date = item.product_exipire_date

    session.commit()
    return itemObject
@app.delete("/{id}")
def deleteItem(id: int, session: Session = Depends(get_session)):
    itemObject = session.query(models.Item).get(id)
    session.delete(itemObject)
    session.commit()
    session.close()

    return "Item was deleted"