from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

books = [
    {
        "id": 1,
        "title": "Mindset",
        "author": "APJ abdull kalam",
        "published_date": "2008-01-23"
    },
    {
        "id": 2,
        "title": "Physics",
        "author": "Eiestin",
        "published_date": "1980-01-3"
    },
    {
        "id": 3,
        "title": "Chemistry",
        "author": "Alchimist",
        "published_date": "1990-01-13"
    },   
    {
        "id": 4,
        "title": "The Nature",
        "author": "Pulo choyilo",
        "published_date": "1970-03-11"
    }

]

app = FastAPI()

@app.get("/book")
def get_book():
    return books

class Book(BaseModel):
    id: int
    title: str
    author: str
    published_date: str

# adding a new book
@app.post("/book")
def create_book(book: Book): #inherting the book class
    new_book = book.model_dump() # it will covert the book model class into dictionary foramt
    books.append(new_book)

# filter the book based on id
@app.get("/book/{boo_id}")
def filter_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


class BookUpdate(BaseModel):
    title: str
    author: str
    published_date: str

@app.put("/book/{book_id}")
def update_book(book_id: int, update_book: BookUpdate):
    for book in books:
        if book["id"] == book_id:
            book['title'] = update_book.title
            book['author'] = update_book.author
            book['published_date'] = update_book.published_date
            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.delete("/book/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "book deleted successfully"}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Books not found")