from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from db import SessionLocal, engine, Base, database
from models import Book, BookCreate, BookInResponse
from pydantic import BaseModel
from sqlalchemy import select

# Khởi tạo FastAPI
app = FastAPI()

# Tạo các bảng trong cơ sở dữ liệu (nếu chưa có)
Base.metadata.create_all(bind=engine)



# Hàm lấy session để kết nối với cơ sở dữ liệu
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route để lấy tất cả sách
@app.get("/books/", response_model=list[BookInResponse])
async def get_books(db: Session = Depends(get_db)):
    books = db.execute(select(Book)).scalars().all()
    return books

# Route để thêm sách mới
@app.post("/books/", response_model=BookInResponse)
async def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = Book(title=book.title, author=book.author, publish_year=book.publish_year, price=book.price)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Route để lấy sách theo ID
@app.get("/books/{book_id}", response_model=BookInResponse)
async def get_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book
