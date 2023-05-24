import sqlite3

class students:
    def __init__(self):
        self.connection = sqlite3.connect("./moko.db")
        self.connection.row_factory=sqlite3.Row
        self.cur = self.connection.cursor()
  

    def addStudent(self, nom , age , classe ):
        self.cur.execute("""
        INSERT INTO Student(
        nom , age , classes
        VALUES (?,?,?)
        )""",(nom, age, classe))
        self.connection.commit()

    def getStudent(self):
        self.cur.execute("""
        SELECT nom, 
        classe,
        age FROM student""")
        students = self.cur.fetchall()
        return students
    
    def get_student(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    



    
