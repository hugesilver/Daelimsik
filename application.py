from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def main():
    return "Hello It's Daelimsik"

@app.route('/student', methods=["POST"])
def student():
    with open('./data/m_student.json', 'r') as student:
        m_student = json.load(student)
    return m_student

@app.route('/profstaff', methods=["POST"])
def profstaff():
    with open('./data/m_profstaff.json', 'r') as profstaff:
        m_profstaff = json.load(profstaff)
    return m_profstaff

@app.route('/weather', methods=["POST"])
def weather():
    with open('./data/m_weather.json', 'r') as weather:
        m_weather = json.load(weather)
    return m_weather

if __name__ == "__main__":
    app.run(host='0.0.0.0', port= "", debug=True)