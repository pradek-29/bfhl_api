from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def process_array():
    try:
        data = request.json
        arr = data.get("array", [])

        numbers = [x for x in arr if isinstance(x, int)]
        alphabets = [x.upper() for x in arr if isinstance(x, str) and x.isalpha()]
        special_chars = [x for x in arr if isinstance(x, str) and not x.isalnum()]
        evens = [x for x in numbers if x % 2 == 0]
        odds = [x for x in numbers if x % 2 != 0]
        concat = "".join(alphabets)[::-1]

        return jsonify({
            "status": "success",
            "user_id": "12345",
            "email_id": "example@email.com",
            "college_roll_number": "21BCE1234",
            "even_numbers": evens,
            "odd_numbers": odds,
            "alphabets": alphabets,
            "special_characters": special_chars,
            "sum_of_numbers": sum(numbers),
            "reversed_alphabets": concat
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
