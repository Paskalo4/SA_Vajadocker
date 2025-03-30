from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def index():
    return "Zdravo iz strežnika!"

@app.route('/data')
def send_data():
    # Pošljemo časovni žig kot primer podatkov
    return f"Podatki iz strežnika: {time.ctime()}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
