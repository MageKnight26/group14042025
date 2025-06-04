class GroupLimitError(Exception):
    def __init__(self, message="У групі не може бути більше 10 студентів"):
        super().__init__(message)


class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} y.o."


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, record book: {self.record_book}"

    def __hash__(self):
        return hash((self.first_name, self.last_name, self.record_book))

    def __eq__(self, other):
        return (
            isinstance(other, Student)
            and self.first_name == other.first_name
            and self.last_name == other.last_name
            and self.record_book == other.record_book
        )


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupLimitError()
        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        all_students = "\n".join(str(s) for s in self.group)
        return f"Number: {self.number}\n{all_students}"


gr = Group("PD1")

# Додаємо 10 студентів
for i in range(1, 11):
    st = Student("Male", 20 + i, f"Name{i}", f"Surname{i}", f"AN{i}")
    gr.add_student(st)

# Спроба додати 11-го — обробка винятку
try:
    st_extra = Student("Female", 22, "Extra", "Student", "AN999")
    gr.add_student(st_extra)
except GroupLimitError as e:
    print(f"Виняток: {e}")
