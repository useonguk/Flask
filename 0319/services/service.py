import datetime
from models.model import SchoolDB

class SchoolService :
    def __init__(self):
        self.school_db = SchoolDB()
        
    def get_students(self) :
        student_list = []
        students = self.school_db.get_schoolStudent();
        
        for student in students :
            student_dict = {
                "id": student[0],
                "number": student[1],
                "name": student[2],
                "gender": student[3]
            }
            student_list.append(student_dict)
        return student_list
    
    def post_student(self, school_dto):
        self.school_db.post_schoolStudent(school_dto)
        
    def get_course(self):
        course_list = []  
        courses = self.school_db.get_course()

        for course in courses:
            course_dict = {
                "id" : course[0],
                "name": course[1],
                "professor": course[2],
                "credit": course[3]
            }
            course_list.append(course_dict)

        return course_list  
    
    def post_course(self, course_dto) :
        result = self.school_db.get_course()
        for c in result :
            if c[1] == course_dto.name and c[2] == course_dto.professor:
                raise Exception("이 등 과")
        self.school_db.post_course(course_dto)
        
    def get_enrollment(self) :
        list = []
        result = self.school_db.get_enrollment()
        for a in result :
            dit = {
                "student_number" : a[0],
                "student_name" : a[1],
                "course_name" : a[2],
                "professor" : a[3],
                "credit" : a[4],
            }
            list.append(dit)
        
        return list
        
    def add(self, newenroll):
        self.school_db.add(newenroll)
        
    def delete(self, id):
        self.school_db.delete(id)
        
    def get_professor(self):
        list = []
        response = self.school_db.get_professor()
        for a in response:
            dit = {
                "id" : a[0],
                "name" : a[1],
                "major" : a[2],
                "email" : a[3]
            }
            list.append(dit)
        return list
    
    def add_professor(self, newprofessor):
        self.school_db.add_professor(newprofessor)
        
    def get_lecture(self):
        list = []
        response = self.school_db.get_lecture()
        for a in response:
            dit = {
                "course_name" : a[0],
                "professor_name" : a[1],
                "professor_major" : a[2],
                "credit" : a[3],
                "day" : a[4],
                "start_time" : a[5],
                "end_time" : a[6]
            }
            list.append(dit)
        return list
    
    def add_lecture(self, newLecture):
        self.school_db.add_lecture(newLecture)
        
    def delete_lecture(self, id):
        self.school_db.delete_lecture(id)
        
    def get_professor_lectures(self, professor_id):
        professor_lectures = []
        lectures = self.school_db.get_professor_lectures(professor_id)

        for lecture in lectures:
            lecture_dict = {
                "course_name": lecture[0],
                "credit": lecture[1],  # 학점 정보 추가
                "day": lecture[2],
                "start_time": str(lecture[3]),
                "end_time": str(lecture[4]),
            }
            professor_lectures.append(lecture_dict)

        return professor_lectures

    def get_student_lectures(self, student_id):
        student_lectures = []

        # 학생의 강의 정보를 데이터베이스에서 가져옴
        lectures = self.school_db.get_student_lectures(student_id)

        # 각 강의 정보를 딕셔너리로 변환하여 리스트에 추가
        for lecture in lectures:
            # 강의 정보 추출
            course_name = lecture[0]  # 강의명
            day = lecture[1]  # 강의 요일
            start_time = (datetime.datetime.min + lecture[2]).time().strftime('%H')  # 강의 시작 시간 (시:분 형식으로 변환)
            credit = lecture[3]  # 학점

            # 강의 정보를 딕셔너리로 저장
            lecture_dict = {
                "course_name": course_name,
                "day": day,
                "lecture_time": start_time,
                "credit": credit
            }

            # 리스트에 추가
            student_lectures.append(lecture_dict)

        return student_lectures





