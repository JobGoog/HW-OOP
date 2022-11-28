class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
   
    def rate_lecture(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in lecture.courses_attached:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return res



    def __lt__(self, someone):
        if not isinstance(someone, Student):
            print('Такое не сравниваю')
            return
        return self.average_rating < someone.average_rating


        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

        


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self) -> str:
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res

    def __lt__(self, someone):
        if not isinstance(someone, Lecturer):
            print('Такое не сравниваю')
            return
        return self.average_rating < someone.average_rating

    

class Reviewer(Mentor):
 
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self) -> str:
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res


def Avg_grades_Student(self):
    grades_count = 0
    courses_in_progress_string = ', '.join(self.courses_in_progress)
    finished_courses_string = ', '.join(self.finished_courses)
    for k in self.grades:
        grades_count += len(self.grades[k])
    self.average_rating = sum(map(sum, self.grades.values())) / grades_count
    print(f'Средняя оценка за домашнее задание: {self.average_rating}')

def Avg_grades_Lecturer(self):
    grades_count = 0
    for k in self.grades:
        grades_count += len(self.grades[k])
    self.average_rating = sum(map(sum, self.grades.values())) / grades_count
    print(f'Средняя оценка за лекции: {self.average_rating}')


 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('Nice', 'Guy')
cool_lecturer.courses_attached += ['Python']
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

best_student.rate_lecture(cool_lecturer, 'Python', 10)
best_student.rate_lecture(cool_lecturer, 'Python', 9)
best_student.rate_lecture(cool_lecturer, 'Python', 1)

 
print(best_student.grades)
print('')
print(cool_lecturer.grades)
print('')
print(best_student)
print('')
print(cool_lecturer)
print('')
print(cool_reviewer)

Avg_grades_Student(best_student)

Avg_grades_Lecturer(cool_lecturer)