from flask import render_template, request, redirect, url_for, Blueprint
from services.service import SchoolService
from dto import SDto, CDto, EDto


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
