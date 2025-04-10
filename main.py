# main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Customer as CustomerModel
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from typing import Optional


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Solo tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependencia de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Schemas Pydantic
class CustomerCreate(BaseModel):
    imageSrc: Optional[str] = None
    firstName: str
    lastName: str
    street: Optional[str] = None
    zipcode: Optional[int] = None
    city: Optional[str] = None
    phoneNumber: Optional[str] = None
    mail: Optional[str] = None
    labels: Optional[str] = None
    notes: Optional[str] = None

class CustomerUpdate(CustomerCreate):
    pass

class CustomerOut(BaseModel):
    id: int
    imageSrc: Optional[str] = None
    firstName: str
    lastName: str
    street: Optional[str] = None
    zipcode: Optional[int] = None
    city: Optional[str] = None
    phoneNumber: Optional[str] = None
    mail: Optional[str] = None
    labels: Optional[str] = None
    notes: Optional[str] = None

    class Config:
        from_attributes = True

# Endpoints CRUD

@app.get("/customers", response_model=List[CustomerOut])
def get_customers(db: Session = Depends(get_db)):
    customers = db.query(CustomerModel).all()
    return customers

@app.post("/customers", response_model=CustomerOut)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    print("📥 Recibido en POST /customers:", customer.dict())
    db_customer = CustomerModel(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

@app.put("/customers/{customer_id}", response_model=CustomerOut)
def update_customer(customer_id: int, customer: CustomerUpdate, db: Session = Depends(get_db)):
    print("📦 Datos recibidos para actualizar:", customer.dict())
    db_customer = db.query(CustomerModel).filter(CustomerModel.id == customer_id).first()
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    for key, value in customer.dict(exclude_unset=True).items():
        setattr(db_customer, key, value)
    db.commit()
    db.refresh(db_customer)
    return db_customer

@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = db.query(CustomerModel).filter(CustomerModel.id == customer_id).first()
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    db.delete(db_customer)
    db.commit()
    return {"detail": "Customer deleted successfully"}
