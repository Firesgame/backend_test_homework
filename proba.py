import datetime as dt


class Calculator:
    records = []

    def __init__(self, limit):
        self.limit = limit

    def add_record(self, record):
        self.records.append([record.amount, record.comment, record.date])

    def get_today_stats(self):
        today_stats = 0
        for record in self.records:
            if record[2] == dt.datetime.now().date():
                today_stats += record[0]
        return today_stats

    def get_today_remained(self):
        for record in self.records:
            if record[2] == dt.datetime.now().date():
                self.limit -= record[0]
        return self.limit

    def get_week_stats(self):
        week_stats = 0
        for record in self.records:
            if record[2] >= (dt.datetime.now() - dt.timedelta(days=7)).date():
                week_stats += record[0]
        return week_stats


class Record:
    def __init__(self, amount, comment, date=dt.datetime.now()):
        self.amount = amount
        self.comment = comment
        if isinstance(date, str):
            self.date = (dt.datetime.strptime(date, '%d.%m.%Y').date())
        else:
            self.date = date.date()


class CashCalculator(Calculator):
    USD_RATE = 74.39
    EURO_RATE = 81.45

    def add_record(self, record):
        Calculator.add_record(self, record)

    def get_today_stats(self):
        Calculator.get_today_stats(self)

    def get_today_cash_remained(self, currency):
        self.currency = currency
        Calculator.get_today_remained(self)
        if self.currency == 'usd':
            self.limit /= CashCalculator.USD_RATE
            self.currency = 'USD'
        elif self.currency == 'eur':
            self.limit /= CashCalculator.EURO_RATE
            self.currency = 'Euro'
        else:
            self.currency = 'руб'
        if self.limit > 0:
            return f'На сегодня осталось {round(self.limit)} {self.currency}'
        elif self.limit == 0:
            return f'Денег нет, держись'
        else:
            return f'Денег нет, держись: твой долг - ' \
                   f'{round(abs(self.limit))} {self.currency}'

    def get_week_stats(self):
        Calculator.get_week_stats(self)


class CaloriesCalculator(Calculator):

    def __init__(self, limit):
        super().__init__(limit)
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        super().get_today_stats()

    def get_calories_remained(self):
        total = super().get_today_stats()
        answer = self.limit - total
        if answer > 0:
            return f'Можно с {answer} кКал'
        else:
            return 'Хватит есть'

    def get_week_stats(self):
        super().get_week_stats()