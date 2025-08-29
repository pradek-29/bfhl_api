from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/")
async def process_data(request: Request):
    try:
        # Get JSON data from request
        data = await request.json()
        input_array = data.get("input", [])

        # Separate values
        even_numbers = [x for x in input_array if isinstance(x, int) and x % 2 == 0]
        odd_numbers = [x for x in input_array if isinstance(x, int) and x % 2 != 0]
        alphabets = [x.upper() for x in input_array if isinstance(x, str) and x.isalpha()]
        special_chars = [x for x in input_array if isinstance(x, str) and not x.isalnum()]
        sum_numbers = sum([x for x in input_array if isinstance(x, int)])
        reversed_alpha_concat = "".join([x for x in input_array if isinstance(x, str) and x.isalpha()])[::-1].upper()

        # Response JSON
        return JSONResponse({
            "status": "success",
            "user_id": "123456",
            "email": "example@vit.ac.in",
            "roll_number": "22BCE0000",
            "even_numbers": even_numbers,
            "odd_numbers": odd_numbers,
            "alphabets_uppercase": alphabets,
            "special_characters": special_chars,
            "sum_of_numbers": sum_numbers,
            "reversed_alphabets_concat": reversed_alpha_concat
        })

    except Exception as e:
        return JSONResponse({"status": "error", "message": str(e)}, status_code=500)

@app.get("/")
async def home():
    return {"message": "API is working!"}
