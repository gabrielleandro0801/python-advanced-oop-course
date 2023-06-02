class Show:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name.title()

    def give_like(self):
        self._likes += 1


class Movie(Show):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def give_like(self):
        self._likes += 1


class Serie(Show):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons


if __name__ == '__main__':
    fast_x = Movie("Fast X", 2023, 130)
    fast_x.give_like()
    print(fast_x)
