class Employee:
    def __init__(self, name):
        self.name = name

    def register_work_hours(self, hours):
        print(f'{hours} work hours registered')

    def show_tasks(self):
        print('Did many things...')


class Caelum(Employee):
    def show_tasks(self):
        print('Did many things, Caelumer')

    def find_courses_of_month(self, month=None):
        print(f'Showing courses from - {month}' if month else 'Showing courses from this month')


class Alura(Employee):
    def show_tasks(self):
        print('Did many things, Alurete!')

    def find_unanswered_questions(self):
        print('Showing unanswered questions')


class Hipster:
    def __str__(self):
        return f'Hipster,  {self.name}'


class Junior(Alura):
    pass


class Full(Alura, Caelum, Hipster):
    pass


if __name__ == '__main__':
    john = Junior('John')
    john.find_unanswered_questions()
    john.show_tasks()

    mary = Full('Mary')
    mary.find_unanswered_questions()
    mary.find_courses_of_month()

    mary.show_tasks()
    print(mary)
