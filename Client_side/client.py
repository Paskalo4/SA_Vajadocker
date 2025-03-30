from flask import Flask, render_template
import requests

app = Flask(__name__)

# URL strežnika, ki bo poslal podatke
SERVER_URL = "http://server:5000"  # Strežnik se imenuje "server" v omrežju Docker

@app.route('/')
def home():
    try:
        # Pošlje zahtevo na strežnik za pridobitev podatkov
        response = requests.get(f'{SERVER_URL}/data')  # endpoint za prenos podatkov
        data = response.text  # Vzemimo besedilo iz odgovora (lahko bo slika ali besedilo)
        return render_template('index.html', data=data)
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
