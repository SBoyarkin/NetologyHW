class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __count_grades(self):
        return len([grade for grade in self.grades.values() for grade in grade])
    def average_grades(self):
        return sum([grade for grade in self.grades.values() for grade in grade])/self.__count_grades()

    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname} \n'
                f'Средняя оценка за домашние задания: {self.average_grades()}\n'
                f'Курсы в процессе изучения: {self.courses_in_progress}\n'
                f'Завершенные курсы: {self.finished_courses}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __count_grades(self):
        return len([grade for grade in self.grades.values() for grade in grade])
    def average_grades(self):
        if self.__count_grades() > 0:
            return sum([grade for grade in self.grades.values() for grade in grade])/self.__count_grades()
        else:
            return 'Оценок нет'

    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname} \n'
                f'Средняя оценка за лекции: {self.average_grades()}')

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'






some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']
some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python',]

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)

some_lecturer = Lecturer('Some','Boddy')
some_student.rate_hw(some_reviewer, 'Python', 10)
some_lecturer.courses_attached += ['Python']
some_student.rate_hw(some_lecturer, 'Python', 10)







print(some_reviewer)
print('__________')
print(some_lecturer)
print('__________')
print(some_student)

