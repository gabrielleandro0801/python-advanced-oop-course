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

    @property
    def likes(self):
        return self._likes

    def give_like(self):
        self._likes += 1

    def __str__(self):
        return f"Name: {self._name} | Likes: {self._likes}"


class Movie(Show):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def give_like(self):
        self._likes += 1

    def __str__(self):
        return f"Name: {self._name} | Likes: {self._likes} | Duration: {self.duration} min"


class Serie(Show):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f"Name: {self._name} | Likes: {self._likes} | Seasons: {self.seasons}"


if __name__ == '__main__':
    fast_x = Movie("Fast X", 2023, 130)
    fast_x.give_like()

    the_chosen = Serie("The Chosen", 2016, 5)
    the_chosen.give_like()
    the_chosen.give_like()

    movies_and_series = [fast_x, the_chosen]
    for show in movies_and_series:
        print(show)
