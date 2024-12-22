from flask import Flask, render_template, request
import openai
from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder='')
openai.api_key = os.getenv("OPENAI_API_KEY")
messages = []
messages.append({"role": "system", "content": "Kamu adalah asisten virtual yang selalu memberikan jawaban dalam bahasa Indonesia."})
messages.insert(0, {"role": "system", "content": "Kamu adalah asisten AI yang selalu memberikan jawaban dalam bahasa Indonesia. Jangan pernah menjawab dalam bahasa lain."})

# ... (bagian lain dari kode Anda)
def generate_response(user_input):
    # Tambahkan input pengguna ke daftar pesan
    messages.append({"role": "user", "content": user_input})
    try:
        # Panggil API OpenAI dengan model dan pesan
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # Gunakan model yang valid
            messages=messages
        )
        
        # Ekstrak respons dari API
        reply = response.choices[0].message.content
        
        # Tambahkan respons ke daftar pesan
        messages.append({"role": "assistant", "content": reply})
        return reply

    except Exception as e:
        return f"Terjadi kesalahan: {e}"
    
@app.route('/static/<path:filename>')
def custom_static(filename):
    return send_from_directory('static', filename)
@app.route("/", methods=["POST", "GET"])
def chat():
    if request.method == "POST":
        user_input = request.form["user_input"]
        try:
            # ... (kode OpenAI Anda)
            response = generate_response(user_input)
        except Exception as e:
            response = f"Terjadi kesalahan: {e}"
        return render_template("index.html", user_input=user_input, response=response)
    else:
        return render_template("index.html", user_input="", response="")

if __name__ == "__main__":
    app.run(debug=True)