from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/home")
def incio():
    return {"Welcome": "2 the Jungle"}