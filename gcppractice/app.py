import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv('DB_HOST', '127.0.0.1'),
    port=int(os.getenv('DB_PORT', 3307)),
    user=os.getenv('DB_USER', 'sainathdemo'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME', 'Managment_system')
)

cursor = conn.cursor()

cursor.execute("SELECT NOW()")
result = cursor.fetchone()
print("Connected Successfully at:", result[0])

print("\nStudents with marks > 75:")
cursor.execute("""
    SELECT student_id, name, department, marks
    FROM students
    WHERE marks > 75
""")
for row in cursor.fetchall():
    print(row)

print("\nCount of students per department:")
cursor.execute("""
    SELECT department, COUNT(*) AS total_students
    FROM students
    GROUP BY department
""")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()






# from fastapi import FastAPI, Depends, HTTPException
# from pydantic import BaseModel
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.orm import sessionmaker, declarative_base, Session
# from dotenv import load_dotenv
# from urllib.parse import quote_plus
# import os

# load_dotenv()

# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))  
# DB_HOST = os.getenv("DB_HOST")
# DB_PORT = os.getenv("DB_PORT")
# DB_NAME = os.getenv("DB_NAME")

# DATABASE_URL = (
#     f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
#     f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# )


# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
# Base = declarative_base()


# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(100), nullable=False)
#     email = Column(String(100), nullable=False)


# Base.metadata.create_all(bind=engine)

# class UserCreate(BaseModel):
#     name: str
#     email: str

# class UserUpdate(BaseModel):
#     name: str

# class UserResponse(BaseModel):
#     id: int
#     name: str
#     email: str


# app = FastAPI(title="FastAPI + Google Cloud SQL CRUD")


# @app.get("/")
# def root():
#     return {"message": "FastAPI Cloud SQL API is running 🚀"}


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.post("/users", response_model=UserResponse)
# def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = User(name=user.name, email=user.email)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


# @app.get("/users", response_model=list[UserResponse])
# def get_users(db: Session = Depends(get_db)):
#     return db.query(User).all()


# @app.get("/users/{user_id}", response_model=UserResponse)
# def get_user(user_id: int, db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user

# @app.put("/users/{user_id}", response_model=UserResponse)
# def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")

#     user.name = user_update.name
#     db.commit()
#     db.refresh(user)
#     return user

# @app.delete("/users/{user_id}")
# def delete_user(user_id: int, db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")

#     db.delete(user)
#     db.commit()
#     return {"message": "User deleted successfully"}
