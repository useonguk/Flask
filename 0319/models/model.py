import pymysql

class SchoolDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='0000', db='holy')
        self.cur = self.db.cursor()
        print("connect ok") 
        
    def get_schoolStudent(self) :
        sql = "SELECT * FROM student"
        self.cur.execute(sql)
        # self.db.commit()
        return self.cur.fetchall() 
    
    def post_schoolStudent(self, school_dto):
        # 중복 체크 SQL 쿼리
        check_sql = "SELECT * FROM student WHERE number = %s"
        self.cur.execute(check_sql, (school_dto.studentNumber,))
        result = self.cur.fetchone()
        
        if result:
            # 이미 등록된 학생 번호가 존재하는 경우
            print("이미 등록된 학생 번호입니다.")
            return False
        else:
            # 중복이 없는 경우, 삽입 SQL 쿼리 실행
            insert_sql = "INSERT INTO student (number, name, gender) VALUES (%s, %s, %s)"
            values = (school_dto.studentNumber, school_dto.name, school_dto.gender)
            self.cur.execute(insert_sql, values)
            self.db.commit()
            print("학생 등록이 완료되었습니다.")
            return True

        
    def get_course(self):
        sql = "SELECT * FROM course"
        self.cur.execute(sql)
        return self.cur.fetchall()
    
    def post_course(self, course_dto) :
        sql = "INSERT INTO course (name, professor, credit) VALUES (%s, %s, %s)"
        self.cur.execute(sql, (course_dto.name, course_dto.professor, course_dto.credit))
        self.db.commit()
        print("co뭐시기 등록")
        
    def get_enrollment(self):
        sql = """
        SELECT s.number, s.name AS student_name, c.name AS course_name, c.professor, c.credit
        FROM enrollment e
        JOIN student s ON e.student_id = s.id
        JOIN course c ON e.course_id = c.id
        """
        self.cur.execute(sql)
        return self.cur.fetchall()
    
    def post_enrollment(self, dto) :
        sql = "INSERT INTO enrollment (student_id, course_id) VALUES (%s, %s)"
        self.cur.execute(sql, (dto.uid, dto.cid))
        self.db.commit()
        
    def add(self, newenroll):
        check_enroll_sql = "SELECT COUNT(*) FROM enrollment WHERE student_id = %s AND course_id = %s"
        self.cur.execute(check_enroll_sql, (newenroll.student_id, newenroll.course_id))
        enroll_exists = self.cur.fetchone()[0]

        if enroll_exists <= 0:
            sql = "INSERT INTO enrollment (student_id, course_id) VALUES (%s, %s)"
            self.cur.execute(sql, (newenroll.student_id, newenroll.course_id))
            self.db.commit()


    def delete(self, id):
        sql = "delete from enrollment where id={0}".format(id)
        self.cur.execute(sql);
        self.db.commit();
