class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade


class Course:
    students = []
    
    def __init__(self, name, max_students) -> None:
        self.name = name
        self.max_students = max_students

    def add_student(self, student) -> bool:
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_avrage_grade(self) -> float:
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value/len(self.students)



if __name__=="__main__":
    course = Course('science', 2)
    s1 = Student("Tim", 19, 95)
    s2 = Student("Bill", 19, 75)
    s3 = Student("Jill", 19, 65)

    print(course.add_student(s1))
    print(course.add_student(s2))
    print(course.add_student(s3))

    print(course.get_avrage_grade())
