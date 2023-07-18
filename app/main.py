from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"version": "v0.0.4"}
