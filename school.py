class Taecher():
    def teacher(self):
        print('Преподаватель учит')

class School():
    def __init__(self, new_tacher):
        self.teacher = new_tacher

    def start_lesson(self):
        self.teacher.teach()

my_teacher = Taecher()
my_school = School(my_teacher)
