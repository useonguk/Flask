from flask import render_template, request, redirect, url_for, Blueprint, jsonify
from services.service import SchoolService
from dto import LDto, PDto, SDto, CDto, EDto
from datetime import datetime

school_blueprint = Blueprint('school', __name__)
school_service = SchoolService()

@school_blueprint.route('/')
def index():
    return render_template('index.html')

@school_blueprint.route('/student_management', methods=['GET'])
def getStudent():
    
    students = school_service.get_students()

    return render_template('student_management.html',students=students )

@school_blueprint.route('/register_student', methods=['POST'])
def postStudent():
    school_dto = SDto(
        student_number=request.form['number'],
        name=request.form['name'],
        gender=request.form['gender']
    )
    print(school_dto)
    school_service.post_student(school_dto)
    return render_template("index.html")  # 또는 다른 유효한 응답을 반환합니다.

@school_blueprint.route('/course_management', methods=['GET'])
def GetCourse():
    courses = school_service.get_course();
    return render_template("course_management.html", courses=courses)

@school_blueprint.route('/register_course', methods=['POST'])
def PostCourse() :
    course_dto = CDto(
        name = request.form['name'],
        professor = request.form['professor'],
        credit = request.form['credit']
    )
    print(course_dto)
    school_service.post_course(course_dto)
    return render_template("index.html")

@school_blueprint.route('/enrollment_management', methods=['GET'])
def get_enrollment_management():
    
    students = school_service.get_students()
    courses = school_service.get_course()
    enrollments = school_service.get_enrollment()
    
    return render_template("enrollment_management.html", students = students, courses = courses, enrollments=enrollments) 
                                                    
@school_blueprint.route('/register_enrollment', methods=['POST'])
def register():
    student_id = request.form['student_id']
    course_id = request.form['course_id']
    
    # Check if both student_id and course_id are not empty strings
    if student_id and course_id:
        newenroll = EDto(
            _student_id=int(student_id),
            _course_id=int(course_id)
        )
        school_service.add(newenroll)
    
    return redirect(url_for('.index'))

@school_blueprint.route('/cancel_enrollment', methods=['POST'])
def remove():
    enrollment_id = request.form['enrollment_id']
    
    # Check if enrollment_id is not an empty string
    if enrollment_id:
        school_service.delete(enrollment_id)
    
    return redirect(url_for('.index'))

@school_blueprint.route('/professor_management', methods=['GET'])
def get_professor_management() :
    professor = school_service.get_professor()
    return render_template("professor_management.html", professors = professor)

@school_blueprint.route('/lecture_management', methods=['GET'])
def get_lecture_management():
    lecture = school_service.get_lecture()
    professor = school_service.get_professor()
    course = school_service.get_course()
    return render_template("lecture_management.html", lectures = lecture, professors = professor, courses = course  )

@school_blueprint.route('/register_professor', methods=['POST'])
def post_professor():
    name = request.form["name"]
    major = request.form["major"]
    email = request.form["email"]
    
    # Check if name, major, and email are not empty strings
    if name and major and email:
        new_professor = PDto(
            name=name,
            major=major,
            email=email
        )
        school_service.add_professor(new_professor)
    
    return redirect(url_for('.index'))

@school_blueprint.route('/register_lecture', methods=['POST'])
def post_lecture():
    professor_id = request.form["professor_id"]
    course_id = request.form["course_id"]
    day = request.form["day"]
    start_time = request.form["start_time"]
    end_time = request.form["end_time"]
    
    # Check if professor_id, course_id, day, start_time, and end_time are not empty strings
    if professor_id and course_id and day and start_time and end_time:
        new_lecture = LDto(
            professor_id=professor_id,
            course_id=course_id,
            day=day,
            start_time=start_time,
            end_time=end_time
        )
        school_service.add_lecture(new_lecture)
    
    return redirect(url_for('.index'))

@school_blueprint.route('/cancel_lecture', methods=['POST'])
def delete_lecture():
    lecture_id = request.form.get('lecture_id')
        
    # Lecture ID가 제대로 전달되었는지 확인
    if lecture_id:
        # 데이터베이스에서 해당 강의 삭제
        school_service.delete_lecture(lecture_id)

    return redirect(url_for('.index'))

@school_blueprint.route("/api/student/time-table/<int:student_id>", methods=['GET'])
def get_student_time_table(student_id):
    student_lectures = school_service.get_student_lectures(student_id)
    
    # timedelta 객체를 문자열로 변환하여 lectures 리스트 갱신
    lectures = []
    for item in student_lectures:
        lecature_name = str(item["course_name"])
        day = item["day"]
        lecture_time_str = str(item['start_time'])
        lecture_duration_str = str(item['end_time'])
        lectures.append({
            'lecture_time': lecture_time_str,
            'lecture_duration': lecture_duration_str
        })
    
    # 데이터를 JSON 형식으로 변환하여 반환
    response = jsonify({
        "lecture_name" : lecature_name,
        "day" : day,
        'student_id': student_id,
        'lectures': lectures
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@school_blueprint.route("/api/professor/time-table/<int:professor_id>", methods=['GET'])
def get_professor_time_table(professor_id):
    professor_lectures = school_service.get_professor_lectures(professor_id)
    
    # timedelta 객체를 문자열로 변환하여 lectures 리스트 갱신
    lectures = []
    for item in professor_lectures:
        course_name = item["course_name"]
        credit = item["credit"]  # 학점 정보 가져오기
        day = item["day"]
        start_time = datetime.strptime(item['start_time'], '%H:%M:%S')  # 시작 시간을 datetime 객체로 변환
        end_time = datetime.strptime(item['end_time'], '%H:%M:%S')  # 종료 시간을 datetime 객체로 변환
        lectures.append({
            "course_name": course_name,
            "credit": credit,  # 학점 정보 추가
            "day": day,
            'lecture_time': start_time.strftime('%H'),  # 문자열로 다시 변환하여 저장
            'lecture_end': end_time.strftime('%H')  # 문자열로 강의 기간 저장
        })
        
    # 데이터를 JSON 형식으로 변환하여 반환
    response = jsonify({
        'professor_id': professor_id,
        'lectures': lectures
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@school_blueprint.route("/api/course/time-table/<int:student_id>", methods=['GET'])
def get_course_time_table(student_id):
    student_lectures = school_service.get_student_lectures(student_id)
    
    return jsonify({
        'student_id': student_id,
        'lectures': student_lectures
    })