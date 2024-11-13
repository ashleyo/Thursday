''' 
Model People at our College. 
People are either Staff or Students. 
People have a forename and a surname.
Lecturers have a Department and a Staff ID.
Students have a Student ID.
There are also Courses which have a name and a code.
Courses have members who are either Staff or Students.
Courses can list their members.
'''
[ChatGPT](https://chatgpt.com/share/bcd3ff9f-5101-4314-a5f0-64881a22aa39)
'''
(Model) [People] at our [College].
[People] are either [Staff] or [Students].
[People] have a [forename] and a [surname].
[Staff] have a [Department] and a [Staff] [ID].
[Students] have a [Student] [ID].
There are also [Courses] which have a [name] and a [code].
[Courses] have [members] who are either [Staff] or [Students].
[Courses] can (list) their [members].
'''

'''
Three Rs

Robust Reliable Reusable
'''

class Course:
    
        def __init__(self, name, code):
            self.name = name
            self.code = code
            self.members = []
        
        def add_member(self, person):
            self.members.append(person)
        
        def list_members(self):
            print(f'Members of {self.name} ({self.code}):')
            for member in self.members:
                print(member)
            

class Person:

    def __init__(self, forename, surname):
        self.forename = forename
        self.surname = surname
    
    def __str__(self):
        return f'{self.surname}, {self.forename} '

class Staff(Person):

    def __init__(self, forename, surname, department, staff_id):
        super().__init__(forename, surname)
        self.department = department
        self.staff_id = staff_id
    
    def __str__(self):
        return f'{self.staff_id}: {super().__str__()} Dept:{self.department}'
    

class Student(Person):

    def __init__(self, forename, surname, student_id):
        super().__init__(forename, surname)
        self.student_id = student_id

    def __str__(self):
        return f'{super().__str__()} ({self.student_id})'

L = Staff('John', 'Doe', 'Maths', 'X123')
S1 = Student('Jane', 'Smith', 'Y123')
S2 = Student('Alice', 'Jones', 'Y124')
C = Course('Maths 101', 'M101')

C.add_member(L)
C.add_member(S1)
C.add_member(S2)
C.list_members()
