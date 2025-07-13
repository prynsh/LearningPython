from fastapi import APIRouter,status,HTTPException
from typing import List

from src.books.book_data import books
from src.books.schemas import Book, UpdateBook

book_router = APIRouter()


@book_router.get("/", response_model=List[Book])
async def getBooks():
    return books
 

@book_router.post("/",status_code=status.HTTP_201_CREATED)
async def create_books(bookData:Book) -> dict:
    new_book = bookData.model_dump()
    books.append(new_book)
    return new_book

@book_router.get("/{book_id}")
async def getOneBook(book_id:int):
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
        )


@book_router.patch("/{book_id}")
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

