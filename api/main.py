from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Any

app = FastAPI()

class InputData(BaseModel):
    data: List[Any]

@app.get("/")
def home():
    return {"message": "API is working fine!"}

@app.post("/process")
def process_array(input_data: InputData):
    data = input_data.data
    numbers = [x for x in data if isinstance(x, (int, float))]
    alphabets = [x.upper() for x in data if isinstance(x, str) and x.isalpha()]
    special_chars = [x for x in data if isinstance(x, str) and not x.isalnum()]

    even_nums = [x for x in numbers if isinstance(x, int) and x % 2 == 0]
    odd_nums = [x for x in numbers if isinstance(x, int) and x % 2 != 0]
    sum_nums = sum(numbers)
    concat_alpha = "".join(alphabets)[::-1]

    return JSONResponse(content={
        "status": "success",
        "user_id": "123456",
        "email": "abc@example.com",
        "college_roll": "21BCE0000",
        "even_numbers": even_nums,
        "odd_numbers": odd_nums,
        "alphabets": alphabets,
        "special_characters": special_chars,
        "sum_of_numbers": sum_nums,
        "reversed_alphabets": concat_alpha
    })
