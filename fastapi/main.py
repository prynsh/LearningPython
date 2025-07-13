from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import List
app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_date": "2021-01-01",
        "page_count": 1234,
        "language": "English",
    },
    {
        "id": 2,
        "title": "Django By Example",
        "author": "Antonio Mele",
        "publisher": "Packt Publishing Ltd",
        "published_date": "2022-01-19",
        "page_count": 1023,
        "language": "English",
    },
    {
        "id": 3,
        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "publisher": "O'Reilly Media",
        "published_date": "2020-07-20",
        "page_count": 792,
        "language": "English",
    },
    {
        "id": 4,
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "publisher": "No Starch Press",
        "published_date": "2019-05-03",
        "page_count": 544,
        "language": "English",
    },
    {
        "id": 5,
        "title": "Automate the Boring Stuff with Python",
        "author": "Al Sweigart",
        "publisher": "No Starch Press",
        "published_date": "2018-11-01",
        "page_count": 504,
        "language": "English",
    },
    {
        "id": 6,
        "title": "Effective Python",
        "author": "Brett Slatkin",
        "publisher": "Addison-Wesley",
        "published_date": "2020-03-15",
        "page_count": 480,
        "language": "English",
    }
]

class Book(BaseModel):
    id : int
    title : str
    author : str
    publisher : str
    published_date : str
    page_count  : int
    language : str  

class UpdateBook(BaseModel):
    title : str
    author : str
    publisher : str
    page_count  : int
    language : str  


@app.get("/books", response_model=List[Book])
async def getBooks():
    return books
 

@app.post("/books",status_code=status.HTTP_201_CREATED)
async def create_books(bookData:Book) -> dict:
    new_book = bookData.model_dump()
    books.append(new_book)
    return new_book

@app.get("/book/{book_id}")
async def getOneBook(book_id:int):
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
        )


@app.put("/update_book")
async def update_book(book_id:int, updated_book_info:UpdateBook)-> dict:
    for book in books:
        if book['id'] == book_id:
            book['title'] = updated_book_info.title
            book['author'] = updated_book_info.author
            book['publisher'] = updated_book_info.publisher
            book['page_count'] = updated_book_info.page_count
            book['language'] = updated_book_info.language
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"   
    )

