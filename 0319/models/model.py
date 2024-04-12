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
        
    def get_professor(self):
        sql = "SELECT * FROM professor"
        self.cur.execute(sql)
        return self.cur.fetchall()
    
    def add_professor(self, newprofessor):
        # 이미 존재하는 교수인지 확인하는 SQL 쿼리
        check_sql = "SELECT EXISTS (SELECT 1 FROM professor WHERE name = %s AND major = %s AND email = %s)"
        self.cur.execute(check_sql, (newprofessor.name, newprofessor.major, newprofessor.email))
        result = self.cur.fetchone()[0]

        if result:
            # 이미 등록된 교수인 경우
            print("이미 등록된 교수입니다.")
            return False
        else:
            # 중복이 없는 경우, 삽입 SQL 쿼리 실행
            insert_sql = "INSERT INTO professor (name, major, email) VALUES (%s, %s, %s)"
            values = (newprofessor.name, newprofessor.major, newprofessor.email)
            self.cur.execute(insert_sql, values)
            self.db.commit()
            print("교수 등록이 완료되었습니다.")
            return True
        
    def get_lecture(self):
        sql = """SELECT c.name, p.name, p.major, c.credit, l.day, l.start_time, l.end_time
                FROM lecture l
                JOIN course c ON l.course_id = c.id
                JOIN professor p ON l.professor_id = p.id;"""
        self.cur.execute(sql)
        return self.cur.fetchall()
    
    def add_lecture(self, newLecture):
        # 중복 체크 SQL 쿼리
        check_sql = """
            SELECT * 
            FROM lecture 
            WHERE professor_id = %s 
            AND course_id = %s 
            AND day = %s 
            AND start_time = %s 
            AND end_time = %s
        """
        # 중복 체크에 사용할 값들
        check_values = (
            newLecture.professor_id,
            newLecture.course_id,
            newLecture.day,
            newLecture.start_time,
            newLecture.end_time
        )
        # 중복 체크 쿼리 실행
        self.cur.execute(check_sql, check_values)
        result = self.cur.fetchone()
        
        if result:
            # 이미 해당 강의가 등록되어 있는 경우
            print("이미 해당 강의가 등록되어 있습니다.")
            return False
        else:
            # 중복이 없는 경우, 삽입 SQL 쿼리 실행
            insert_sql = """
                INSERT INTO lecture (professor_id, course_id, day, start_time, end_time)
                VALUES (%s, %s, %s, %s, %s)
            """
            # 강의 정보를 삽입하는 쿼리 실행
            insert_values = (
                newLecture.professor_id,
                newLecture.course_id,
                newLecture.day,
                newLecture.start_time,
                newLecture.end_time
            )
            self.cur.execute(insert_sql, insert_values)
            # 변경 사항 커밋
            self.db.commit()
            print("강의 등록이 완료되었습니다.")
            return True
        
    def add_lecture(self, newLecture):
        # 삽입하기 전에 시간이 겹치는 강의가 있는지 확인
        check_sql = """
            SELECT * 
            FROM lecture 
            WHERE day = %s 
            AND (
                (start_time >= %s AND start_time < %s)
                OR (end_time > %s AND end_time <= %s)
                OR (start_time <= %s AND end_time >= %s)
            )
        """
        check_values = (
            newLecture.day,
            newLecture.start_time,
            newLecture.end_time,
            newLecture.start_time,
            newLecture.end_time,
            newLecture.start_time,
            newLecture.end_time
        )
        self.cur.execute(check_sql, check_values)
        existing_lecture = self.cur.fetchone()
        
        if existing_lecture:
            print("이미 해당 시간대에 강의가 등록되어 있습니다.")
            return False
        else:
            # 삽입 SQL 쿼리 작성
            insert_sql = """
                INSERT INTO lecture (professor_id, course_id, day, start_time, end_time)
                VALUES (%s, %s, %s, %s, %s)
            """
            # 강의 정보를 삽입하는 쿼리 실행
            insert_values = (
                newLecture.professor_id,
                newLecture.course_id,
                newLecture.day,
                newLecture.start_time,
                newLecture.end_time
            )
            self.cur.execute(insert_sql, insert_values)
            # 변경 사항 커밋
            self.db.commit()
            print("강의 등록이 완료되었습니다.")
            return True

    
    def delete_lecture(self, id):
        sql = "DELETE FROM lecture WHERE id = %s"
        self.cur.execute(sql, (id))
        self.db.commit()
        
    def get_professor_lectures(self, professor_id):
        sql = """
            SELECT c.name AS course_name, c.credit, l.day, l.start_time, l.end_time
            FROM lecture l
            JOIN course c ON l.course_id = c.id
            WHERE l.professor_id = %s
        """
        self.cur.execute(sql, (professor_id,))
        return self.cur.fetchall()

    
    def get_student_lectures(self,  student_id):
        sql = """
            SELECT c.name AS course_name, l.day, l.start_time, c.credit
            FROM enrollment e
            JOIN lecture l ON e.course_id = l.course_id
            JOIN course c ON e.course_id = c.id
            WHERE e.student_id = %s
        """
        self.cur.execute(sql, (student_id,))
        return self.cur.fetchall()




    
    
