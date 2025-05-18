from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
{'title': 'Title Two', 'author': 'Author Two', 'category': 'Math'},
{'title': 'Title Three', 'author': 'Author Three', 'category': 'History'},
{'title': 'Title Four', 'author': 'Author Four', 'category': 'Engineering'},
{'title': 'Title Five', 'author': 'Author Five', 'category': 'Engineering'},
{'title': 'Title Six', 'author': 'Author Six', 'category': 'History'}
]

@app.get("/books")
async def read_all_books():
    return BOOKS

# @app.get("/books/{dynamic_param}")
# async def read_all_books(dynamic_param: str):
#     return {'dynamic_param': dynamic_param}


@app.get("/books/{book_title}")
async def read_all_books(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
        return None
    return None