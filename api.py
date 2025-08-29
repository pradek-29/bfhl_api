from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class InputData(BaseModel):
    data: List[str]

# Helper function for alternating caps
def alternating_caps(s: str) -> str:
    result = ""
    upper = True
    for ch in s:
        if ch.isalpha():
            result += ch.upper() if upper else ch.lower()
            upper = not upper
        else:
            result += ch
    return result

@app.post("/bfhl")
async def process_data(input_data: InputData):
    data = input_data.data
    odd_numbers, even_numbers, alphabets, special_chars = [], [], [], []
    numbers_sum = 0
    alphabets_concat = ""

    for item in data:
        if item.isdigit():
            num = int(item)
            (even_numbers if num % 2 == 0 else odd_numbers).append(item)
            numbers_sum += num
        elif item.isalpha():
            alphabets.append(item.upper())
            alphabets_concat += item
        else:
            special_chars.append(item)

    concat_string = alternating_caps(alphabets_concat[::-1])

    return {
        "is_success": True,
        "user_id": "john_doe_17091999",
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "alphabets": alphabets,
        "special_characters": special_chars,
        "sum": str(numbers_sum),
        "concat_string": concat_string
    }
