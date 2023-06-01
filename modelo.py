class Movie:
    def __init__(self, name, year, duration):
        self.__name = name.title()
        self.year = year
        self.duration = duration
        self.__likes = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name.title()

    def give_like(self):
        self.__likes += 1


class Serie:
    def __init__(self, name, year, seasons):
        self.__name = name.title()
        self.year = year
        self.seasons = seasons
        self.__likes = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name.title()

    def give_like(self):
        self.__likes += 1


if __name__ == '__main__':
    fast_x = Movie("Fast X", 2023, 140)
    fast_x.give_like()
    print(fast_x)
