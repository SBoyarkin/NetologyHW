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

    def __get_count_grades(self):
        return len([grade for grade in self.grades.values() for grade in grade])

    def get_average_grades(self):
        return sum([grade for grade in self.grades.values() for grade in grade])/self.__get_count_grades()

    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname} \n'
                f'Средняя оценка за домашние задания: {self.get_average_grades():.1f}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def __lt__(self, other):
        return self.get_average_grades() < other.get_average_grades()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __get_count_grades(self):
        return len([grade for grade in self.grades.values() for grade in grade])

    def get_average_grades(self):
        if self.__get_count_grades() > 0:
            return sum([grade for grade in self.grades.values() for grade in grade])/self.__get_count_grades()
        else:
            return 'Оценок нет'

    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname} \n'
                f'Средняя оценка за лекции: {self.get_average_grades()}')

    def __lt__(self, other):
        return self.get_average_grades() < other.get_average_grades()


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
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname}')


some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']
some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python', 'Git']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 10)

some_lecturer = Lecturer('Some', 'Boddy')
some_lecturer.courses_attached += ['Python']
some_student.rate_hw(some_lecturer, 'Python', 5)
some_student.rate_hw(some_lecturer, 'Python', 10)

print(some_reviewer)
print('__________')
print(some_lecturer)
print('__________')
print(some_student)

s1 = Student('Ivan', 'Ivanov', 'm')
s2 = Student('Sergey', 'Sergeev', 'm')
l1 = Lecturer('Olga', 'Bogdanova')
l2 = Lecturer('Tatyana', 'Mikhailova')

l1.courses_attached += ['Python']
l2.courses_attached += ['Python', 'Git', 'JavaScript']
s1.courses_in_progress += ['Python']
s2.courses_in_progress += ['Python', 'Git']
some_reviewer.rate_hw(s1, 'Python', 4)
some_reviewer.rate_hw(s1, 'Python', 8)
some_reviewer.rate_hw(s2, 'Python', 8)
some_reviewer.rate_hw(s2, 'Git', 2)

s1.rate_hw(l1, 'Python', 5)
s1.rate_hw(l1, 'Python', 8)
s1.rate_hw(l1, 'Python', 10)
s1.rate_hw(l2, 'Python', 4)
s1.rate_hw(l2, 'Python', 7)
s1.rate_hw(l2, 'Python', 1)

print(s1.get_average_grades())
print(s2.get_average_grades())

student_list = [s1, s2]
lecturer_list = [l1, l2]


def get_avg_studens(students, course):
    grades_list = []
    for studen in students:
        if course in studen.grades.keys():
            grades_list += studen.grades.get(course)
    return print(f'{sum(grades_list)/len(grades_list):.1f}')


def get_avg_lecturer(lecturers, course):
    grades_list = []
    for lecturer in lecturers:
        if course in lecturer.grades.keys():
            grades_list += lecturer.grades.get(course)
    return print(f'{sum(grades_list)/len(grades_list):.1f}')


get_avg_studens(student_list, 'Python')
get_avg_lecturer(lecturer_list, 'Python')
