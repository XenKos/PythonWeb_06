import sqlite3
import faker
from random import randint, choice
from datetime import datetime
import sqlite3

NUMBER_STUDENTS = 30
NUMBER_TEACHERSS = 5
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = 8
NUMBER_GRADES = 20

def generate_fake_data(number_students, number_teachers, number_groups, number_subjects, number_grades) -> tuple:
    fake = Faker()

    fake_students = []  
    fake_teachers = []  
    fake_groups = []  
    fake_subjects = []
    fake_grades = []

    # Генерация фейковых данных для students
    for _ in range(number_students):
        name = fake.name()
        gender = fake.random_element(elements=('Male', 'Female'))
        date_of_birth = fake.date_of_birth(minimum_age=15, maximum_age=25)
        email = fake.email()
        fake_students.append((name, gender, date_of_birth, email))

    # Генерация фейковых данных для groups
    for group_id in range(1, number_groups + 1):
        group_name = f"Group {group_id}"
        numbers_of_students = random.randint(20, 30)
        year_established = fake.date_time_between(start_date='-10y', end_date='now').year
        fake_groups.append((group_name, numbers_of_students, year_established))

    # Генерация фейковых данных для teachers
    for _ in range(number_teachers):
        teacher_name = fake.name()
        position = fake.job()
        email = fake.email()
        fake_teachers.append((teacher_name, position, email))

    # Генерация фейковых данных для subjects
    subjects = ['Math', 'Science', 'History', 'English', 'Physics', 'Biology', 'Chemistry', 'Geography', 'Literature']
    for _ in range(number_subjects):
        subject_name = random.choice(subjects)
        teacher_id = random.randint(1, number_teachers)  # Assuming teacher IDs start from 1
        fake_subjects.append((subject_name, teacher_id))

    # Генерация фейковых данных для grades
    for student_id in range(1, number_students + 1):
        for _ in range(random.randint(10, number_grades)):
            subject_id = random.randint(1, number_subjects)  # Assuming subject IDs start from 1
            grade = random.randint(1, 100)
            date_received = fake.date_time_between(start_date='-1y', end_date='now').strftime('%Y-%m-%d')
            fake_grades.append((student_id, subject_id, grade, date_received))

    return fake_students, fake_teachers, fake_groups, fake_subjects, fake_grades

def prepare_data(students, teachers, groups, subjects, grades) -> tuple:
    for_students = []
    # Дополнительные операции с данными, если необходимо
    return students, teachers, groups, subjects, grades

# Вызов функций для генерации и подготовки данных
students, teachers, groups, subjects, grades = prepare_data(*generate_fake_data(NUMBER_STUDENTS, NUMBER_TEACHERS, NUMBER_GROUPS, NUMBER_SUBJECTS, NUMBER_GRADES))

# Вывод результатов
print("Students:")
for student in students:
    print(student)

print("\nTeachers:")
for teacher in teachers:
    print(teacher)

print("\nGroups:")
for group in groups:
    print(group)

print("\nSubjects:")
for subject in subjects:
    print(subject)

print("\nGrades:")
for grade in grades:
    print(grade)