class SDto:
    def __init__(self, student_number, name, gender):
        self._student_number = student_number
        self._name = name
        self._gender = gender
        
    @property
    def studentNumber(self):
        return self._student_number
    
    @property
    def name(self):
        return self._name
    
    @property
    def gender(self):
        return self._gender
    
class CDto:
    def __init__(self, professor, name, credit):
        self._name = name
        self._professor = professor
        self._credit = credit
        
    @property
    def professor(self):
        return self._professor
    
    @property
    def name(self):
        return self._name
    
    @property
    def credit(self):
        return self._credit
    
class EDto:
    def __init__(self, _student_id, _course_id):
        self.student_id = _student_id
        self.course_id = _course_id
        
    @property
    def enroll_student_id(self):
        return self.student_id

    @property
    def enroll_course_id(self):
        return self.course_id
    
class PDto:
    def __init__(self, name, major, email):
        self._name = name
        self._marjor = major
        self._email = email
        
    @property
    def name(self):
        return self._name
    
    @property
    def major(self):
        return self._marjor
    
    @property
    def email(self):
        return self._email
    
class LDto:
    def __init__(self, professor_id, course_id, day, start_time, end_time):
        self._professor_id = professor_id
        self._course_id = course_id
        self._day = day
        self._start_time = start_time
        self._end_time = end_time
    
    @property
    def professor_id(self):
        return self._professor_id
    
    @property
    def course_id(self):
        return self._course_id
    
    @property
    def day(self):
        return self._day
    
    @property
    def start_time(self):
        return self._start_time
    
    @property
    def end_time(self):
        return self._end_time
