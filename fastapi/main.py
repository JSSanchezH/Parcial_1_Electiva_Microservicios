from fastapi import FastAPI

app = FastAPI()

@app.get("/data")
def get_data():
    return {
        "attribute1": "value1",
        "attribute2": "value2",
        "attribute3": "value3",
        "attribute4": "value4",
        "attribute5": "value5"
    }