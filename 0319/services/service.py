from models.model import SchoolDB

class SchoolService :
    def __init__(self):
        self.school_db = SchoolDB()
        
    def get_students(self) :
        student_list = []
        students = self.school_db.get_schoolStudent();
        
        for student in students :
            student_dict = {
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