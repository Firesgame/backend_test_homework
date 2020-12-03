everyone = []


def feed_all():
    for i in everyone:
        if i.calories > 0:
            print(f'{i.name} был покормлен на {i.calories} Ккал')
        else:
            print(f'{i.name} наелcя за день')


class Record:
    def __init__(self, amount, comment):
        self.amount = amount
        self.comment = comment


class All:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.calories = self.limit
        everyone.append(self)

    def sleep(self):
        return "Спит"

    def eat(self, record):
        self.calories = self.calories - record.amount
        return self.calories

    def main_activity(self):
        return 'Это животное может что-то делать'


class Animal(All):

    def run(self):
        return 'Бежит'

    def main_activity(self):
        super().main_activity()
        return 'Это животное бегает'


class Bird(All):
    def fly(self):
        return "Летит"

    def main_activity(self):
        super().main_activity()
        return 'Это животное летает'


class Fish(All):
    def swim(self):
        return 'Плывёт'

    def main_activity(self):
        super().main_activity()
        return 'Это животное плавает'


class Dove(Bird, Animal):
    def main_activity(self):
        super(Dove, self).main_activity()
        return 'Это животное и бегает, и летает'


class Begemot(Animal, Fish):
    def main_activity(self):
        super().main_activity()
        return 'Это животное плавает и бегает'


golub = Dove("Борис", 1000)
ignat = Begemot('игнат', 2000)
golub.eat(Record(250, 'Мяско'))
ignat.eat(Record(3000, 'JFJF'))
golub.eat(Record(550, 'Мяско'))

feed_all()
