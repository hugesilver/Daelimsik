from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def main():
    return "<h2>Hello It's Daelimsik</h2>"

# 학생식당

@app.route('/student', methods=["POST"])
def student():
    with open('./out/student/m_student.json', 'r') as student:
        m_student = json.load(student)
    return m_student

@app.route('/student/mon', methods=["POST"])
def student_mon():
    with open('./out/student/m_student_mon.json', 'r') as student_mon:
        m_student_mon = json.load(student_mon)
    return m_student_mon

@app.route('/student/tue', methods=["POST"])
def student_tue():
    with open('./out/student/m_student_tue.json', 'r') as student_tue:
        m_student_tue = json.load(student_tue)
    return m_student_tue

@app.route('/student/wed', methods=["POST"])
def student_wed():
    with open('./out/student/m_student_wed.json', 'r') as student_wed:
        m_student_wed = json.load(student_wed)
    return m_student_wed

@app.route('/student/thu', methods=["POST"])
def student_thu():
    with open('./out/student/m_student_thu.json', 'r') as student_thu:
        m_student_thu = json.load(student_thu)
    return m_student_thu

@app.route('/student/fri', methods=["POST"])
def student_fri():
    with open('./out/student/m_student_fri.json', 'r') as student_fri:
        m_student_fri = json.load(student_fri)
    return m_student_fri

# 교직원식당

@app.route('/profstaff', methods=["POST"])
def profstaff():
    with open('./out/profstaff/m_profstaff.json', 'r') as profstaff:
        m_profstaff = json.load(profstaff)
    return m_profstaff

@app.route('/profstaff/mon', methods=["POST"])
def profstaff_mon():
    with open('./out/profstaff/m_profstaff_mon.json', 'r') as profstaff_mon:
        m_profstaff_mon = json.load(profstaff_mon)
    return m_profstaff_mon

@app.route('/profstaff/tue', methods=["POST"])
def profstaff_tue():
    with open('./out/profstaff/m_profstaff_tue.json', 'r') as profstaff_tue:
        m_profstaff_tue = json.load(profstaff_tue)
    return m_profstaff_tue

@app.route('/profstaff/wed', methods=["POST"])
def profstaff_wed():
    with open('./out/profstaff/m_profstaff_mon.json', 'r') as profstaff_wed:
        m_profstaff_wed = json.load(profstaff_wed)
    return m_profstaff_wed

@app.route('/profstaff/thu', methods=["POST"])
def profstaff_thu():
    with open('./out/profstaff/m_profstaff_thu.json', 'r') as profstaff_thu:
        m_profstaff_thu = json.load(profstaff_thu)
    return m_profstaff_thu

@app.route('/profstaff/fri', methods=["POST"])
def profstaff_fri():
    with open('./out/profstaff/m_profstaff_fri.json', 'r') as profstaff_fri:
        m_profstaff_fri = json.load(profstaff_fri)
    return m_profstaff_fri

# 공지사항

@app.route('/bachelor', methods=["POST"])
def bachelor():
    with open('./out/announcement/l_bachelor.json', 'r') as bachelor:
        l_bachelor = json.load(bachelor)
    return l_bachelor

@app.route('/scholarship', methods=["POST"])
def scholarship():
    with open('./out/announcement/l_scholarship.json', 'r') as scholarship:
        l_scholarship = json.load(scholarship)
    return l_scholarship

@app.route('/administrative', methods=["POST"])
def administrative():
    with open('./out/announcement/l_administrative.json', 'r') as administrative:
        l_administrative = json.load(administrative)
    return l_administrative

# 학사일정

@app.route('/schedule', methods=["POST"])
def schedule():
    with open('./out/schedule/m_schedule.json', 'r') as schedule:
        m_schedule = json.load(schedule)
    return m_schedule

# 셔틀버스

@app.route('/anyang_to_school', methods=["POST"])
def anyang_to_school():
    with open('./out/schoolbus/m_anyang_to_school.json', 'r') as anyang_to_school:
        m_anyang_to_school = json.load(anyang_to_school)
    return m_anyang_to_school

@app.route('/school_to_anyang', methods=["POST"])
def school_to_anyang():
    with open('./out/schoolbus/m_school_to_anyang.json', 'r') as school_to_anyang:
        m_school_to_anyang = json.load(school_to_anyang)
    return m_school_to_anyang

@app.route('/beomgye_to_school', methods=["POST"])
def beomgye_to_school():
    with open('./out/schoolbus/m_beomgye_to_school.json', 'r') as beomgye_to_school:
        m_beomgye_to_school = json.load(beomgye_to_school)
    return m_beomgye_to_school

@app.route('/school_to_beomgye', methods=["POST"])
def school_to_beomgye():
    with open('./out/schoolbus/m_school_to_beomgye.json', 'r') as school_to_beomgye:
        m_school_to_beomgye = json.load(school_to_beomgye)
    return m_school_to_beomgye

if __name__ == "__main__":
    app.run(host='0.0.0.0', port="", debug=True)