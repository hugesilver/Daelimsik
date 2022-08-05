from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def main():
    return "<h2>Hello It's Daelimsik</h2>"

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

@app.route('/bachelor', methods=["POST"])
def bachelor():
    with open('./data/l_bachelor.json', 'r') as bachelor:
        l_bachelor = json.load(bachelor)
    return l_bachelor

@app.route('/scholarship', methods=["POST"])
def scholarship():
    with open('./data/l_scholarship.json', 'r') as scholarship:
        l_scholarship = json.load(scholarship)
    return l_scholarship

@app.route('/administrative', methods=["POST"])
def administrative():
    with open('./data/l_administrative.json', 'r') as administrative:
        l_administrative = json.load(administrative)
    return l_administrative

if __name__ == "__main__":
    app.run(host='0.0.0.0', port="", debug=True)