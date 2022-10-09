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

@app.route('/schedule', methods=["POST"])
def schedule():
    with open('./data/m_schedule.json', 'r') as schedule:
        m_schedule = json.load(schedule)
    return m_schedule

@app.route('/anyang_to_school', methods=["POST"])
def anyang_to_school():
    with open('./data/m_anyang_to_school.json', 'r') as anyang_to_school:
        m_anyang_to_school = json.load(anyang_to_school)
    return m_anyang_to_school

@app.route('/school_to_anyang', methods=["POST"])
def school_to_anyang():
    with open('./data/m_school_to_anyang.json', 'r') as school_to_anyang:
        m_school_to_anyang = json.load(school_to_anyang)
    return m_school_to_anyang

@app.route('/beomgye_to_school', methods=["POST"])
def beomgye_to_school():
    with open('./data/m_beomgye_to_school.json', 'r') as beomgye_to_school:
        m_beomgye_to_school = json.load(beomgye_to_school)
    return m_beomgye_to_school

@app.route('/school_to_beomgye', methods=["POST"])
def school_to_beomgye():
    with open('./data/m_school_to_beomgye.json', 'r') as school_to_beomgye:
        m_school_to_beomgye = json.load(school_to_beomgye)
    return m_school_to_beomgye

if __name__ == "__main__":
    app.run(host='0.0.0.0', port="", debug=True)