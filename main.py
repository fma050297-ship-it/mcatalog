from fastapi import FastAPI

app = FastAPI(
    title="Movie Catalog API",
    description="API для управления каталогом фильмов",
    version="1.0.0",
)


@app.get("/")
def read_root():
    return {"message": "Welcome to Movie Catalog API!"}
