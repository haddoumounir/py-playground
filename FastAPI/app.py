from fastapi import FastAPI


app = FastAPI()


@app.get("/name/{names}")
def sayMyName(names):
    return "hello " + names
