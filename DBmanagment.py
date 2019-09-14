import sqlite3


class DBmanage:
    def __init__(self,constring):
        self.conn = sqlite3.connect(constring)
        self.c = self.conn.cursor()

    def add_Students(self , ID , name , family):
        cmd = "INSERT INTO students VALUES (? ,? ,?)"
        p = (ID , name , family)
        self.c.execute(cmd,p)
        self.conn.commit()

    def add_Professors(self,Code,name,family,rate):
        cmd = "INSERT INTO Professors VALUES (? ,? ,? ,?)"
        p = (Code, name, family, rate)
        self.c.execute(cmd, p)
        self.conn.commit()

    def add_Courses(self,Code,name,unit,PCode):
        cmd = "INSERT INTO Courses VALUES (?,?,?,?)"
        p = (Code,name,unit,PCode)
        self.c.execute(cmd,p)
        self.conn.commit()

    def add_Marks(self,i,ms,Mark):
        cmd = "INSERT INTO Marks VALUES (?,? ,?)"
        p = (i,ms, Mark)
        self.c.execute(cmd, p)
        self.conn.commit()

    def selectstudentsid(self):
        cmd = "select id from students"
        self.c.execute(cmd)
        list = self.c.fetchall()
        return list

    def selectstudentsname(self):
        cmd = "select name from students"
        self.c.execute(cmd)
        list = self.c.fetchall()
        return list

    def selectstudentsfamily(self):
        cmd = "select family from students"
        self.c.execute(cmd)
        list = self.c.fetchall()
        return list

    def select_id_professors(self):
        cmd = "select Code from Professors"
        self.c.execute(cmd)
        list = self.c.fetchall()
        return list

    def select_Courses_Code(self):
        cmd = "select Code from Courses"
        self.c.execute(cmd)
        list = self.c.fetchall()
        return list

    def select_Course_name(self ,code):
        cmd = "select name from Courses where Code = (?)"
        p = (code)
        self.c.execute(cmd,p)
        Cname = self.c.fetchall()
        return Cname

    def selectCoursesUnit(self,code):
        cmd = "select unit from Courses where code = (?)"
        p = code
        self.c.execute(cmd , p)
        list = self.c.fetchall()
        return list

    def select_Professors_Name(self ,code):
        cmd = "select name from Professors where Code in (select PCode from Courses where Code = (?))"
        p = (code)
        self.c.execute(cmd,p)
        Cname = self.c.fetchall()
        return Cname

    def select_Professors_Family(self ,code):
        cmd = "select family from Professors where Code in (select PCode from Courses where Code = (?))"
        p = (code)
        self.c.execute(cmd,p)
        Cname = self.c.fetchall()
        return Cname

    def Calculatig_Avg(self,x,b):
        cmd = "select Sum(Mark) from Marks where id = ? and ms = ?"
        su = self.c.execute("select SUM(unit) from Courses").fetchall()
        p = (x , b)
        self.c.execute(cmd,p)
        CALA = self.c.fetchall()
        CALAf = CALA[0][0]/su[0][0]
        return CALAf

    def countstudents(self):
        cmd = "select count(id) from students"
        self.c.execute(cmd)
        l = self.c.fetchall()
        return l

    def countprofessors(self):
        cmd = "select count(Code) from Professors"
        self.c.execute(cmd)
        l = self.c.fetchall()
        return l

    def countCourses(self):
        cmd = "select count(Code) from Courses"
        self.c.execute(cmd)
        l = self.c.fetchall()
        return l